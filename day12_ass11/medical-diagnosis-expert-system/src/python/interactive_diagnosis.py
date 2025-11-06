# interactive_diagnosis.py

import subprocess
import shlex
import sys
import re

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
    ('unexplained_weight_loss', 'Unexplained weight loss'),
]

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
    names = []
    for m in re.finditer(r'^---\s+([^\s(]+)', out, flags=re.M):
        names.append(m.group(1))
    return names

def adaptive_dialog():
    s = []
    r = []
    asked = set()

    print("Adaptive symptom questioning (heuristic). I'll ask high-value Qs first.")
    for sv in _sev_checks:
        if sv in asked:
            continue
        lbl = sv.replace('_',' ').capitalize()
        if a_ask(f"Do you have {lbl}?"):
            s.append(sv)
            print("Severe sign reported — will escalate and run inference now.")
            out = run_case(s, r)
            return out

    for k,q in _r:
        if a_ask(q):
            r.append(k)
        asked.add(k)
        out = run_case(s, r)
        names = parse_diags(out)
        if len(names) == 1:
            return out

    for k,q in _m:
        if k in asked:
            continue
        if a_ask(q):
            s.append(k)
        asked.add(k)
        out = run_case(s, r)
        names = parse_diags(out)
        if len(names) == 1:
            return out
        if 0 < len(names) <= 2:
            return out

    return run_case(s, r)

def adaptive_dialog_layered():
    s = []
    r = []
    asked = set()

    def prompt_for(k):
        for a,q in _m:
            if a == k: return q
        for a,q in _r:
            if a == k: return q
        return k.replace('_',' ').capitalize()

    for sv in _sev_checks:
        q = sv.replace('_',' ').capitalize()
        if a_ask(f"Are you having {q} (sudden or severe)?"):
            s.append(sv)
            return run_case(s, r)

    screening = ['fever','cough','abdominal_pain','red_itchy_rash',
                 'painful_urination','excessive_thirst','weight_loss','flashbacks','joint_pain']
    for k in screening:
        if k in asked: continue
        if a_ask(prompt_for(k)):
            s.append(k)
        asked.add(k)

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
        if a_ask("Frequent urination?"): s.append('frequent_urination')
        if a_ask("Cloudy urine?"): s.append('cloudy_urine')
        if a_ask("Previous UTIs?"): r.append('previous_uti')
        if a_ask("Family history of diabetes?"): r.append('family_history_of_diabetes')

    if 'excessive_thirst' in s or 'frequent_urination' in s:
        if a_ask(prompt_for('family_history_of_diabetes')): r.append('family_history_of_diabetes')

    if a_ask("Have you had recent antibiotics or steroids?"):
        r.append('recent_antibiotics_or_steroids')
    if a_ask("Are you immunosuppressed or on long-term steroids?"):
        r.append('immunosuppressed')
    if a_ask("No recent flu vaccine?"):
        r.append('no_recent_vaccination')

    out = run_case(s, r)
    names = parse_diags(out)

    if len(names) > 1:
        if a_ask("Do you smoke?"):
            r.append('smoking_history')
        if a_ask("Any recent travel to malaria areas?"):
            r.append('travel_to_endemic_regions')
        out = run_case(s, r)

    return out

def run_tests():
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

    loc_map = {
        'chest': {'lung_carcinoma','influenza'},
        'abdomen': {'ibs','uti','fungal_infection'},
        'joint': {'osteoarthritis'},
        'urine': {'uti','diabetes_type2'},
        'general': set(dm.keys()),
    }

    def score_now(cands):
        scores = {d:0 for d in cands}
        for d in cands:
            v = dm[d]
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

    pain = a_ask("Do you have any pain right now?")
    if pain:
        if a_ask("Is it chest pain?"):
            s.append('chest_pain')
            loc = 'chest'
        elif a_ask("Is it abdominal pain?"):
            s.append('abdominal_pain')
            loc = 'abdomen'
        elif a_ask("Is it joint pain?"):
            s.append('joint_pain')
            loc = 'joint'
        elif a_ask("Is it pain while peeing?"):
            s.append('painful_urination')
            loc = 'urine'
        else:
            loc = 'general'
    else:
        loc = 'general'

    cands = set(loc_map.get(loc, loc_map['general']))
    if not cands:
        cands = set(dm.keys())

    for k,q in _r:
        if k in ('travel_to_endemic_regions','no_recent_vaccination','smoking_history','previous_uti','family_history_of_diabetes','immunosuppressed'):
            if a_ask(q):
                r.append(k)
            asked.add(k)

    if loc == 'chest':
        if a_ask("Do you have a cough?"): s.append('cough')
        if a_ask("Shortness of breath?"): s.append('shortness_of_breath')
        if a_ask("Any blood when coughing?"): s.append('blood_in_sputum')
        if a_ask("Do you smoke?"): r.append('smoking_history')

    if loc == 'abdomen':
        if a_ask("Bloating or change in bowel habit?"):
            if a_ask("Bloating?"): s.append('bloating')
            if a_ask("Diarrhea or constipation?"): s.append('diarrhea_or_constipation')
        if a_ask("Recent antibiotics or steroids?"): r.append('recent_antibiotics_or_steroids')

    if loc == 'joint':
        if a_ask("Is the joint stiff?"): s.append('stiffness')
        if a_ask("Is there swelling?"): s.append('swelling')
        if a_ask("Any long-term joint problems or injury?"): r.append('prior_joint_injury')

    if loc == 'urine':
        if a_ask("Frequent urination?"): s.append('frequent_urination')
        if a_ask("Cloudy urine?"): s.append('cloudy_urine')
        if a_ask("Previous UTIs?"): r.append('previous_uti')
        if a_ask("Family history of diabetes?"): r.append('family_history_of_diabetes')

    sev_by_d = {
        'malaria': ['organ_failure','cerebral_malaria','jaundice'],
        'influenza': ['difficulty_breathing','chest_pain','severe_fatigue'],
        'lung_carcinoma': ['difficulty_breathing','weight_loss'],
        'schizophrenia': ['intense_hallucinations','inability_to_function'],
        'osteoarthritis': ['chronic_pain','joint_deformity'],
        'ibs': ['chronic_severe_pain','significant_bowel_dysfunction'],
        'fungal_infection': ['systemic_fungal_infection','deep_tissue_involvement'],
        'uti': ['flank_pain','fever_with_nausea'],
        'ptsd': ['chronic_flashbacks','severe_emotional_distress'],
        'diabetes_type2': ['diabetic_ketoacidosis','organ_damage'],
    }
    sev_prompt = {
        'organ_failure': 'Very low urine output, severe confusion or very yellow skin/eyes?',
        'cerebral_malaria': 'Seizures, severe confusion or loss of consciousness?',
        'jaundice': 'Yellowing of the skin or eyes?',
        'difficulty_breathing': 'Is breathing very difficult right now?',
        'chest_pain': 'Are you having severe chest pain?',
        'severe_fatigue': 'Are you extremely weak or hard to wake?',
        'inability_to_function': 'Unable to carry out normal daily activities?',
        'intense_hallucinations': 'Seeing or hearing things that are not there and very distressed?',
        'chronic_pain': 'Is the pain constant and severe, limiting movement?',
        'joint_deformity': 'Noticeable deformity or inability to use the joint?',
        'chronic_severe_pain': 'Long‑standing severe abdominal pain?',
        'significant_bowel_dysfunction': 'Severe ongoing diarrhea or obstruction signs?',
        'systemic_fungal_infection': 'High fever with spreading skin involvement or sickness?',
        'deep_tissue_involvement': 'Deep sore or spreading redness and fever?',
        'flank_pain': 'Pain on the side of your lower back (flank)?',
        'fever_with_nausea': 'Fever with vomiting or severe nausea?',
        'chronic_flashbacks': 'Ongoing uncontrollable flashbacks causing distress?',
        'severe_emotional_distress': 'Severe panic/very distressed and unsafe?',
        'diabetic_ketoacidosis': 'Very rapid breathing, vomiting or confusion (possible DKA)?',
        'organ_damage': 'Symptoms suggesting serious organ problem (liver/kidney)?',
    }
    rel_sev = []
    if loc == 'general':
        rel_sev = ['difficulty_breathing','chest_pain','organ_failure']
    else:
        for d in cands:
            for sv in sev_by_d.get(d, []):
                if sv not in asked and sv not in rel_sev:
                    rel_sev.append(sv)
    for sv in rel_sev:
        if sv in asked:
            continue
        asked.add(sv)
        if sv == 'difficulty_breathing':
            q = sev_prompt.get(sv, 'Is breathing very difficult right now?')
            if a_ask(q):
                if a_ask("Did this start suddenly (minutes–hours)?"):
                    s.append(sv)
                    print("Acute severe breathing difficulty — escalating and running inference now.")
                    return run_case(s, r)
                else:
                    if 'smoking_history' in r or a_ask("Do you smoke or have a long-term cough?"):
                        s.append('persistent_cough')
                        continue
                    else:
                        s.append(sv)
                        print("Breathing difficulty noted — running inference now.")
                        return run_case(s, r)
        else:
            qtxt = sev_prompt.get(sv, sv.replace('_',' ').capitalize() + ' now?')
            if a_ask(qtxt):
                s.append(sv)
                print("Urgent sign reported — escalating and running inference now.")
                return run_case(s, r)

    dis_map = {
        'malaria':[('fever','Fever'),('chills','Chills'),('sweating','Sweating')],
        'influenza':[('fever','Fever'),('cough','Cough'),('fatigue','Fatigue')],
        'lung_carcinoma':[('persistent_cough','Persistent cough'),('blood_in_sputum','Blood in sputum'),('weight_loss','Weight loss')],
        'osteoarthritis':[('joint_pain','Joint pain'),('stiffness','Stiffness'),('swelling','Swelling')],
        'ibs':[('abdominal_pain','Abdominal pain'),('bloating','Bloating')],
        'uti':[('painful_urination','Painful urination'),('frequent_urination','Frequent urination')],
        'diabetes_type2':[('excessive_thirst','Excessive thirst'),('frequent_urination','Frequent urination')],
    }

    pool = []
    for d in cands:
        pool.extend(dis_map.get(d, []))
    seen = set(); pool2 = []
    for k,lab in pool:
        if k not in seen:
            seen.add(k); pool2.append((k,lab))
    pool = pool2

    max_q = 6
    asked_q = 0
    while asked_q < max_q:
        scores = {d:0 for d in cands}
        for d in cands:
            v = dm[d]
            for ss in s:
                if ss in v['sym']: scores[d] += 2
                if ss in _sev_checks: scores[d] += 5
            for rr in r:
                if rr in v['risk']: scores[d] += 3

        top, conf, gap = top_candidate(scores)
        if conf >= 0.6 or gap >= 3 or (top and scores[top] >= 6):
            break
        next_q = None
        for k,lab in pool:
            if k in s or k in asked:
                continue
            next_q = (k, lab); break
        if not next_q:
            break
        k, lab = next_q
        asked.add(k); asked_q += 1
        if a_ask(lab):
            s.append(k)
        scores = {d:0 for d in cands}
        for d in cands:
            v = dm[d]
            for ss in s:
                if ss in v['sym']: scores[d] += 2
            for rr in r:
                if rr in v['risk']: scores[d] += 3
        items = sorted(scores.items(), key=lambda x:-x[1])
        if items and items[0][1] - (items[1][1] if len(items)>1 else 0) >= 3:
            topd = items[0][0]
            cands = {topd}

    out = run_case(s, r)
    return out

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ('--test','-t'):
        ok = run_tests()
        sys.exit(0 if ok else 2)

    print("Stepwise adaptive check — will start general then refine.")
    out = adaptive_prob_dialog()
    print("\nResult:\n")
    print(out)

if __name__ == '__main__':
    main()