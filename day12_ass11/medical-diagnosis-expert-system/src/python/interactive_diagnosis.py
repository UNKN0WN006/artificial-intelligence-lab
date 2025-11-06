# interactive_diagnosis.py

import subprocess
import shlex
import sys
import re

# mapping: (prolog_atom, prompt)
_m = [
    ('fever', 'Fever'),
    ('chills', 'Chills'),
    ('sweating', 'Sweating'),
    ('cough', 'Cough'),
    ('fatigue', 'Fatigue'),
    ('sore_throat', 'Sore throat'),
    ('runny_nose', 'Runny nose'),
    ('persistent_cough', 'Persistent cough'),
    ('blood_in_sputum', 'Blood in sputum'),
    ('shortness_of_breath', 'Shortness of breath'),
    ('weight_loss', 'Weight loss'),
    ('joint_pain', 'Joint pain'),
    ('stiffness', 'Stiffness'),
    ('abdominal_pain', 'Abdominal pain'),
    ('bloating', 'Bloating'),
    ('diarrhea_or_constipation', 'Diarrhea or constipation'),
    ('red_itchy_rash', 'Red/itchy rash'),
    ('painful_urination', 'Painful/burning urination'),
    ('frequent_urination', 'Frequent urination'),
    ('cloudy_urine', 'Cloudy urine'),
    ('flashbacks', 'Flashbacks / intrusive memories'),
    ('excessive_thirst', 'Excessive thirst'),
    ('frequent_urination', 'Frequent urination (diabetes)'),
    ('unexplained_weight_loss', 'Unexplained weight loss'),
]

# risk/factors mapping
_r = [
    ('travel_to_endemic_regions', 'Travel to malaria-endemic region'),
    ('previous_malaria', 'Previous malaria history'),
    ('immunosuppressed', 'Weak immune system / immunosuppressed'),
    ('no_recent_vaccination', 'No recent flu vaccination'),
    ('asthma_or_copd', 'Asthma or COPD'),
    ('smoking_history', 'Smoking history'),
    ('family_history_of_diabetes', 'Family history of diabetes'),
    ('obesity', 'Obesity'),
    ('sedentary_lifestyle', 'Sedentary lifestyle'),
    ('history_of_trauma', 'History of trauma (PTSD risk)'),
    ('previous_uti', 'Previous UTI'),
]

# compact list of severe indicators (from KB severe_symptom entries)
_sev_checks = [
    'organ_failure','cerebral_malaria','jaundice',
    'difficulty_breathing','chest_pain','severe_fatigue',
    'inability_to_function','intense_hallucinations',
    'chronic_pain','joint_deformity',
    'chronic_severe_pain','significant_bowel_dysfunction',
    'systemic_fungal_infection','deep_tissue_involvement',
    'flank_pain','fever_with_nausea',
    'chronic_flashbacks','severe_emotional_distress',
    'diabetic_ketoacidosis','organ_damage'
]

def a_ask(q):
    a = input(q + " (yes/no): ").strip().lower()
    return a.startswith('y')

def mk_list(lst):
    if not lst:
        return '[]'
    return '[' + ','.join(lst) + ']'

def run_case(slist, rlist, timeout=20):
    sl = mk_list(slist)
    rl = mk_list(rlist)
    cmd = f"swipl -q -s src/prolog/knowledge_base.pl -g \"run_diag({sl},{rl}),halt.\""
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    out = p.stdout.strip()
    if p.returncode != 0:
        out = (p.stderr.strip() or out) + ("\n[rc=%s]" % p.returncode)
    return out

def parse_diags(out):
    # find lines like: --- malaria (severe) ---
    names = []
    for m in re.finditer(r'^---\s+([^\s(]+)', out, flags=re.M):
        names.append(m.group(1))
    return names

def adaptive_dialog():
    s = []
    r = []
    asked = set()

    print("Adaptive symptom questioning (heuristic). I'll ask high-value Qs first.")
    # 1) severe checks first — if any yes, add and stop (escalate)
    for sv in _sev_checks:
        if sv in asked:
            continue
        lbl = sv.replace('_',' ').capitalize()
        if a_ask(f"Do you have {lbl}?"):
            s.append(sv)
            print("Severe sign reported — will escalate and run inference now.")
            out = run_case(s, r)
            return out

    # 2) risk factors next, checking after each to narrow differentials
    for k,q in _r:
        if a_ask(q):
            r.append(k)
        asked.add(k)
        out = run_case(s, r)
        names = parse_diags(out)
        if len(names) == 1:
            # single candidate found, stop early
            return out
        # otherwise continue asking

    # 3) core symptoms, ask iteratively and re-run to check narrowing
    for k,q in _m:
        if k in asked:
            continue
        if a_ask(q):
            s.append(k)
        asked.add(k)
        out = run_case(s, r)
        names = parse_diags(out)
        # stop if single candidate or small set
        if len(names) == 1:
            return out
        # heuristic stop: if <=2 candidates, accept and show them
        if 0 < len(names) <= 2:
            return out

    # final pass: no decisive single candidate — run full inference and return whatever
    return run_case(s, r)

def adaptive_dialog_layered():
    s = []
    r = []
    asked = set()

    # quick helper to map atom->prompt lookup in _m/_r
    def prompt_for(k):
        for a,q in _m:
            if a == k: return q
        for a,q in _r:
            if a == k: return q
        return k.replace('_',' ').capitalize()

    # severe checks first but phrased simply
    for sv in _sev_checks:
        q = sv.replace('_',' ').capitalize()
        if a_ask(f"Are you having {q} (sudden or severe)?"):
            s.append(sv)
            return run_case(s, r)  # escalate, immediate inference

    # stage 1: simple screening (few plain Qs)
    screening = ['fever','cough','abdominal_pain','red_itchy_rash',
                 'painful_urination','excessive_thirst','weight_loss','flashbacks','joint_pain']
    for k in screening:
        if k in asked: continue
        if a_ask(prompt_for(k)):
            s.append(k)
        asked.add(k)

    # targeted followups based on positives
    if 'fever' in s:
        for k in ('chills','sweating'):
            if a_ask(prompt_for(k)): s.append(k)
        if a_ask(prompt_for('travel_to_endemic_regions')): r.append('travel_to_endemic_regions')

    if 'cough' in s or 'persistent_cough' in s:
        for k in ('blood_in_sputum','shortness_of_breath'):
            if a_ask(prompt_for(k)): s.append(k)
        if a_ask(prompt_for('smoking_history')): r.append('smoking_history')

    if 'abdominal_pain' in s:
        for k in ('bloating','diarrhea_or_constipation'):
            if a_ask(prompt_for(k)): s.append(k)

    if 'painful_urination' in s:
        if a_ask(prompt_for('previous_uti')): r.append('previous_uti')
        if a_ask(prompt_for('diabetes')): r.append('diabetes')  # fallback; may not be in _r

    if 'excessive_thirst' in s or 'frequent_urination' in s:
        if a_ask(prompt_for('family_history_of_diabetes')): r.append('family_history_of_diabetes')

    # quick history questions if still unclear
    if a_ask("Have you had recent antibiotics or steroids?"):
        r.append('recent_antibiotics_or_steroids')
    if a_ask("Are you immunosuppressed or on long-term steroids?"):
        r.append('immunosuppressed')
    if a_ask("No recent flu vaccine?"):
        r.append('no_recent_vaccination')

    # run inference now
    out = run_case(s, r)
    names = parse_diags(out)

    # if still ambiguous, ask discriminators (one or two)
    if len(names) > 1:
        # pick a few high-value discriminators
        if a_ask("Do you smoke?"):
            r.append('smoking_history')
        if a_ask("Any recent travel to malaria areas?"):
            r.append('travel_to_endemic_regions')
        out = run_case(s, r)

    return out

def run_tests():
    # quick integration cases: (symptoms, risks, expected_disease_substr)
    tcs = [
        (['fever','chills','sweating'], ['travel_to_endemic_regions'], 'malaria'),
        (['fever','cough','fatigue'], ['no_recent_vaccination'], 'influenza'),
        (['persistent_cough','blood_in_sputum','weight_loss'], ['smoking_history'], 'lung_carcinoma'),
        (['abdominal_pain','bloating'], ['stress_or_anxiety'], 'ibs'),
        (['painful_urination','frequent_urination'], ['previous_uti'], 'uti'),
        (['excessive_thirst','frequent_urination'], ['family_history_of_diabetes'], 'diabetes_type2'),
    ]
    ok = 0
    bad = 0
    for i,(s,r,exp) in enumerate(tcs,1):
        print(f"\nTC{i}: s={s} r={r} -> expect '{exp}'")
        o = run_case(s,r)
        print("OUT:\n", o)
        if exp in o:
            print("-> PASS")
            ok += 1
        else:
            print("-> FAIL")
            bad += 1
    print(f"\nRESULT: {ok} passed, {bad} failed")
    return bad == 0

def adaptive_prob_dialog():
    s = []
    r = []
    asked = set()

    # small local KB (mirrors Prolog atoms) for quick scoring
    dm = {
        'malaria': {'sym':{'fever','chills','sweating'}, 'risk':{'travel_to_endemic_regions','previous_malaria','immunosuppressed'}},
        'influenza': {'sym':{'fever','cough','fatigue','sore_throat','runny_nose'}, 'risk':{'no_recent_vaccination','asthma_or_copd','immunosuppressed'}},
        'lung_carcinoma': {'sym':{'persistent_cough','blood_in_sputum','shortness_of_breath','weight_loss','bone_pain'}, 'risk':{'smoking_history','family_history','occupational_exposure'}},
        'schizophrenia': {'sym':{'delusions','hallucinations','disorganized_thinking'}, 'risk':{'family_history','substance_abuse','trauma_history'}},
        'osteoarthritis': {'sym':{'joint_pain','stiffness','swelling'}, 'risk':{'family_history','prior_joint_injury','obesity'}},
        'ibs': {'sym':{'abdominal_pain','bloating','diarrhea_or_constipation'}, 'risk':{'family_history','stress_or_anxiety','antibiotic_use'}},
        'fungal_infection': {'sym':{'red_itchy_rash','scaling_skin','blisters'}, 'risk':{'immunosuppressed','recent_antibiotics_or_steroids'}},
        'uti': {'sym':{'painful_urination','frequent_urination','cloudy_urine','flank_pain'}, 'risk':{'previous_uti','diabetes','sexual_activity'}},
        'ptsd': {'sym':{'flashbacks','avoidance','negative_mood'}, 'risk':{'history_of_trauma','prior_mental_health_conditions'}},
        'diabetes_type2': {'sym':{'excessive_thirst','frequent_urination','unexplained_weight_loss','elevated_blood_sugar'}, 'risk':{'family_history_of_diabetes','obesity','sedentary_lifestyle'}},
    }

    def score_now():
        scores = {d:0 for d in dm}
        for d,v in dm.items():
            for ss in s:
                if ss in v['sym']:
                    scores[d] += 2
                if ss in _sev_checks:
                    scores[d] += 5
            for rr in r:
                if rr in v['risk']:
                    scores[d] += 3
        return scores

    def top_candidate(scores):
        items = sorted(scores.items(), key=lambda x:-x[1])
        if not items: return None,0,0
        top, tscore = items[0]
        second = items[1][1] if len(items) > 1 else 0
        total = sum(scores.values()) or 1
        conf = tscore / total
        gap = tscore - second
        return top, conf, gap

    # 1) general pain screening (very simple)
    if a_ask("Do you have any pain right now?"):
        # location-specific yes/no Qs (add corresponding symptom atoms)
        if a_ask("Is the pain in your chest?"):
            s.append('chest_pain')   # may map to severe indicator for influenza/lung issues
        if a_ask("Is the pain in your abdomen?"):
            s.append('abdominal_pain')
        if a_ask("Is it joint pain?"):
            s.append('joint_pain')
        if a_ask("Is the pain when you pass urine?"):
            s.append('painful_urination')
        if a_ask("Is it severe or limiting you?"):
            # treat as severe generic flag
            s.append('severe_pain')
    # check severe indicators explicitly (escalate)
    for sv in _sev_checks:
        if a_ask(sv.replace('_',' ').capitalize() + " now?"):
            s.append(sv)
            print("Severe feature noted — running immediate inference.")
            return run_case(s, r)

    # quick history/risk screening
    for k,q in _r:
        if a_ask(q):
            r.append(k)

    # iterative scoring loop: ask small discriminators until confident
    dis = [
        ('fever','Fever'),
        ('cough','Cough'),
        ('fatigue','Fatigue'),
        ('chills','Chills'),
        ('sweating','Sweating'),
        ('persistent_cough','Persistent cough'),
        ('blood_in_sputum','Blood in sputum'),
        ('shortness_of_breath','Shortness of breath'),
        ('excessive_thirst','Excessive thirst'),
        ('frequent_urination','Frequent urination'),
        ('red_itchy_rash','Red/itchy rash'),
        ('bloating','Bloating'),
        ('diarrhea_or_constipation','Diarrhea or constipation'),
        ('weight_loss','Weight loss'),
    ]
    max_q = 8
    asked_q = 0
    while asked_q < max_q:
        scores = score_now()
        top, conf, gap = top_candidate(scores)
        # stop if confident enough
        if conf >= 0.6 or gap >= 3 or (top and scores[top] >= 6):
            break
        # pick next discriminator not yet asked
        next_q = None
        for k,lab in dis:
            if k in s or k in asked:
                continue
            next_q = (k, lab)
            break
        if not next_q:
            break
        k, lab = next_q
        asked.add(k)
        asked_q += 1
        if a_ask(lab):
            s.append(k)
        # after each answer, re-evaluate; small early-run to check candidates via Prolog
        out = run_case(s, r)
        names = parse_diags(out)
        if len(names) == 1:
            return out

    # final inference run
    out = run_case(s, r)
    return out

# replace old adaptive call in main() to use adaptive_prob_dialog
def main():
    # allow quick test mode
    if len(sys.argv) > 1 and sys.argv[1] in ('--test','-t'):
        ok = run_tests()
        sys.exit(0 if ok else 2)

    print("Stepwise adaptive check — will start general then refine.")
    out = adaptive_prob_dialog()
    print("\nResult:\n")
    print(out)

if __name__ == '__main__':
    main()