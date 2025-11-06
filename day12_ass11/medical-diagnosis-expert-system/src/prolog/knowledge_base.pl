% Diseases and categories
disease(malaria, infectious).
disease(influenza, respiratory).
disease(lung_carcinoma, cancer).
disease(schizophrenia, mental_health).
disease(osteoarthritis, musculoskeletal).
disease(ibs, gastrointestinal).
disease(fungal_infection, infectious).
disease(uti, urinary).
disease(ptsd, mental_health).
disease(diabetes_type2, endocrine).

% Core symptoms
symptom(malaria, fever).
symptom(malaria, chills).
symptom(malaria, sweating).

symptom(influenza, fever).
symptom(influenza, cough).
symptom(influenza, fatigue).
symptom(influenza, sore_throat).
symptom(influenza, runny_nose).

symptom(lung_carcinoma, persistent_cough).
symptom(lung_carcinoma, blood_in_sputum).
symptom(lung_carcinoma, shortness_of_breath).
symptom(lung_carcinoma, weight_loss).
symptom(lung_carcinoma, bone_pain).

symptom(schizophrenia, delusions).
symptom(schizophrenia, hallucinations).
symptom(schizophrenia, disorganized_thinking).

symptom(osteoarthritis, joint_pain).
symptom(osteoarthritis, stiffness).
symptom(osteoarthritis, swelling).

symptom(ibs, abdominal_pain).
symptom(ibs, bloating).
symptom(ibs, diarrhea_or_constipation).

symptom(fungal_infection, red_itchy_rash).
symptom(fungal_infection, scaling_skin).
symptom(fungal_infection, blisters).

symptom(uti, painful_urination).
symptom(uti, frequent_urination).
symptom(uti, cloudy_urine).
symptom(uti, flank_pain).

symptom(ptsd, flashbacks).
symptom(ptsd, avoidance).
symptom(ptsd, negative_mood).

symptom(diabetes_type2, excessive_thirst).
symptom(diabetes_type2, frequent_urination).
symptom(diabetes_type2, unexplained_weight_loss).
symptom(diabetes_type2, elevated_blood_sugar).

% Severe / advanced indicators
severe_symptom(malaria, organ_failure).
severe_symptom(malaria, cerebral_malaria).
severe_symptom(malaria, jaundice).

severe_symptom(influenza, difficulty_breathing).
severe_symptom(influenza, chest_pain).
severe_symptom(influenza, severe_fatigue).

severe_symptom(lung_carcinoma, difficulty_breathing).
severe_symptom(lung_carcinoma, weight_loss).
severe_symptom(lung_carcinoma, bone_pain).

severe_symptom(schizophrenia, inability_to_function).
severe_symptom(schizophrenia, intense_hallucinations).

severe_symptom(osteoarthritis, chronic_pain).
severe_symptom(osteoarthritis, joint_deformity).

severe_symptom(ibs, chronic_severe_pain).
severe_symptom(ibs, significant_bowel_dysfunction).

severe_symptom(fungal_infection, systemic_fungal_infection).
severe_symptom(fungal_infection, deep_tissue_involvement).

severe_symptom(uti, flank_pain).
severe_symptom(uti, fever_with_nausea).

severe_symptom(ptsd, chronic_flashbacks).
severe_symptom(ptsd, severe_emotional_distress).

severe_symptom(diabetes_type2, diabetic_ketoacidosis).
severe_symptom(diabetes_type2, organ_damage).

% Risk / medical history factors
risk_factor(malaria, travel_to_endemic_regions).
risk_factor(malaria, previous_malaria).
risk_factor(malaria, immunosuppressed).

risk_factor(influenza, no_recent_vaccination).
risk_factor(influenza, asthma_or_copd).
risk_factor(influenza, immunocompromised).

risk_factor(lung_carcinoma, smoking_history).
risk_factor(lung_carcinoma, family_history).
risk_factor(lung_carcinoma, occupational_exposure).

risk_factor(schizophrenia, family_history).
risk_factor(schizophrenia, substance_abuse).
risk_factor(schizophrenia, trauma_history).

risk_factor(osteoarthritis, family_history).
risk_factor(osteoarthritis, prior_joint_injury).
risk_factor(osteoarthritis, obesity).

risk_factor(ibs, family_history).
risk_factor(ibs, stress_or_anxiety).
risk_factor(ibs, antibiotic_use).

risk_factor(fungal_infection, immunosuppressed).
risk_factor(fungal_infection, recent_antibiotics_or_steroids).

risk_factor(uti, previous_uti).
risk_factor(uti, diabetes).
risk_factor(uti, sexual_activity).

risk_factor(ptsd, history_of_trauma).
risk_factor(ptsd, prior_mental_health_conditions).

risk_factor(diabetes_type2, family_history_of_diabetes).
risk_factor(diabetes_type2, obesity).
risk_factor(diabetes_type2, sedentary_lifestyle).

% Diagnostic tests (lists)
tests(malaria, mild, [blood_smear, rapid_diagnostic_test]).
tests(malaria, severe, [blood_smear, rdt, liver_function_tests, admit_for_iv_treatment]).

tests(influenza, mild, [rapid_flu_test]).
tests(influenza, severe, [rapid_flu_test, pcr, chest_xray, admit_for_support]).

tests(lung_carcinoma, early, [chest_xray, ct_scan]).
tests(lung_carcinoma, advanced, [chest_xray, ct_scan, biopsy, oncologic_workup]).

tests(schizophrenia, mild, [psychiatric_evaluation]).
tests(schizophrenia, severe, [psychiatric_evaluation, brain_imaging]).

tests(osteoarthritis, mild, [xray]).
tests(osteoarthritis, severe, [xray, mri, joint_fluid_analysis]).

tests(ibs, mild, [rome_iv_assessment]).
tests(ibs, severe, [stool_tests, colonoscopy]).

tests(fungal_infection, mild, [skin_scraping]).
tests(fungal_infection, severe, [skin_scraping, fungal_culture, biopsy]).

tests(uti, mild, [urinalysis, urine_culture]).
tests(uti, severe, [urinalysis, urine_culture, renal_imaging]).

tests(ptsd, mild, [ptsd_questionnaire, psychiatric_evaluation]).
tests(ptsd, severe, [ptsd_questionnaire, psychiatric_evaluation, intensive_psych_care]).

tests(diabetes_type2, mild, [blood_glucose, hba1c]).
tests(diabetes_type2, severe, [blood_glucose, hba1c, electrolyte_panel, admit_if_dka]).

% Treatments (lists)
treatment(malaria, mild, [oral_antimalarial_chloroquine]).
treatment(malaria, severe, [iv_artesunate, hospitalization]).

treatment(influenza, mild, [rest, hydration, oseltamivir]).
treatment(influenza, severe, [iv_antivirals, hospitalization]).

treatment(lung_carcinoma, early, [surgery_lobectomy, radiation]).
treatment(lung_carcinoma, advanced, [chemotherapy, immunotherapy]).

treatment(schizophrenia, mild, [antipsychotics, therapy]).
treatment(schizophrenia, severe, [intensive_therapy, hospitalization, medication_adjustment]).

treatment(osteoarthritis, mild, [nsaids, physical_therapy, weight_management]).
treatment(osteoarthritis, severe, [joint_replacement, corticosteroid_injections]).

treatment(ibs, mild, [dietary_changes_low_fodmap, fiber_supplements]).
treatment(ibs, severe, [antispasmodics, laxatives, psychotherapy]).

treatment(fungal_infection, mild, [topical_antifungal]).
treatment(fungal_infection, severe, [oral_antifungal, iv_antifungal]).

treatment(uti, mild, [oral_antibiotics]).
treatment(uti, severe, [iv_antibiotics, hospitalization]).

treatment(ptsd, mild, [cbt, emdr, ssris]).
treatment(ptsd, severe, [intensive_therapy, prolonged_exposure, hospitalization_if_needed]).

treatment(diabetes_type2, mild, [lifestyle_modification, metformin]).
treatment(diabetes_type2, severe, [insulin_therapy, additional_medications]).

% Interactive helpers (improved prompts)
humanize(Atom, Label) :-
    atom(Atom),
    atomic_list_concat(Parts, '_', Atom),
    atomic_list_concat(Parts, ' ', Temp),
    ( Temp = '' ->
        Label = Temp
    ;
        sub_atom(Temp, 0, 1, After, FirstAtom),
        sub_atom(Temp, 1, After, 0, RestAtom),
        upcase_atom(FirstAtom, UpperFirst),
        atom_concat(UpperFirst, RestAtom, Label)
    ).

% ask_about prints a readable question for symptom/risk names and accepts yes/y
ask_about(Item) :-
    humanize(Item, Label),
    format('Do you have ~w? (yes/no): ', [Label]),
    read(Response),
    ( Response == yes ; Response == y ).

% Determine severity: severe if any severe indicator reported or explicit severe history;
% otherwise mild if at least two core symptoms reported.
diagnose(Disease, severe) :-
    disease(Disease, _),
    severe_symptom(Disease, Sev),
    ask_about(Sev), !.

diagnose(Disease, severe) :-
    disease(Disease, _),
    risk_factor(Disease, Factor),
    ask_about(Factor), !.

diagnose(Disease, mild) :-
    disease(Disease, _),
    findall(S, symptom(Disease, S), Symptoms),
    count_reported(Symptoms, Count),
    Count >= 2.

% Count how many symptoms in list are reported by user
count_reported([], 0).
count_reported([H|T], N) :-
    ( ask_about(H) -> count_reported(T, N1), N is N1 + 1 ; count_reported(T, N) ).

% Query to run diagnosis for each disease: will ask interactive questions.
run_diagnosis_for(Disease) :-
    format('--- Checking ~w (~w) ---~n', [Disease, Category]),
    disease(Disease, Category),
    ( diagnose(Disease, severe) ->
        format('Possible diagnosis: ~w (SEVERE)~n', [Disease]),
        tests(Disease, severe, Tests), format('Recommended tests: ~w~n', [Tests]),
        treatment(Disease, severe, Treat), format('Suggested treatment: ~w~n', [Treat])
    ; diagnose(Disease, mild) ->
        format('Possible diagnosis: ~w (MILD)~n', [Disease]),
        tests(Disease, mild, Tests), format('Recommended tests: ~w~n', [Tests]),
        treatment(Disease, mild, Treat), format('Suggested treatment: ~w~n', [Treat])
    ; format('Insufficient symptoms to suggest ~w.~n', [Disease])
    ).

% --- Non-interactive inference helpers (for Python wrapper) ---
% count how many of Given symptoms match Disease core symptoms
symptom_match_count(D, Given, N) :-
    findall(S, (symptom(D,S), member(S,Given)), L),
    length(L, N).

has_any_severe(D, Given) :-
    severe_symptom(D, S),
    member(S, Given), !.
has_any_risk(D, Given) :-
    risk_factor(D, R),
    member(R, Given), !.

% map requested generic severity to KB test/treatment keys (special-case lung_carcinoma)
map_key(lung_carcinoma, mild, early).
map_key(lung_carcinoma, severe, advanced).
map_key(_, mild, mild).
map_key(_, severe, severe).

tests_for(D, Severity, Tests) :-
    map_key(D, Severity, K),
    tests(D, K, Tests).
treatment_for(D, Severity, Treat) :-
    map_key(D, Severity, K),
    treatment(D, K, Treat).

% diagnose_from checks given symptom and risk lists (non-interactive)
diagnose_from(SGiven, RGiven, D, severe) :-
    disease(D, _),
    ( has_any_severe(D, SGiven)
    ; has_any_risk(D, RGiven)
    ), !.
diagnose_from(SGiven, _RGiven, D, mild) :-
    disease(D, _),
    symptom_match_count(D, SGiven, C),
    C >= 2, !.

% run a full pass and print readable results
run_diag(SGiven, RGiven) :-
    findall([D, Sev, Tests, Treat],
            ( disease(D,_),
              diagnose_from(SGiven, RGiven, D, Sev) ->
                  tests_for(D, Sev, Tests),
                  treatment_for(D, Sev, Treat)
            ),
            L),
    ( L = [] ->
        format('No likely diagnoses found.~n')
    ;
        forall(member([D,S,Ts,Tr], L),
               ( format('~n--- ~w (~w) ---~n', [D,S]),
                 format('Recommended tests: ~w~n', [Ts]),
                 format('Suggested treatment: ~w~n', [Tr])
               ))
    ).

% optional debug printer
p(L) :- format('~w~n', [L]).