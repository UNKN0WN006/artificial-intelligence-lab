import unittest
import subprocess

class TestIntegration(unittest.TestCase):

    def test_diagnosis_flu(self):
        symptoms = "fever cough sore_throat"
        expected_diagnosis = "flu"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_cold(self):
        symptoms = "cough runny_nose"
        expected_diagnosis = "cold"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_allergy(self):
        symptoms = "sneezing itchy_eyes"
        expected_diagnosis = "allergy"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_stomach_ache(self):
        symptoms = "stomach_pain nausea"
        expected_diagnosis = "stomach_ache"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_migraine(self):
        symptoms = "headache nausea sensitivity_to_light"
        expected_diagnosis = "migraine"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_diabetes(self):
        symptoms = "increased_thirst frequent_urination"
        expected_diagnosis = "diabetes"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_heart_disease(self):
        symptoms = "chest_pain shortness_of_breath"
        expected_diagnosis = "heart_disease"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_asthma(self):
        symptoms = "wheezing shortness_of_breath"
        expected_diagnosis = "asthma"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_pneumonia(self):
        symptoms = "cough fever difficulty_breathing"
        expected_diagnosis = "pneumonia"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def test_diagnosis_anemia(self):
        symptoms = "fatigue weakness pale_skin"
        expected_diagnosis = "anemia"
        self.assertEqual(self.get_diagnosis(symptoms), expected_diagnosis)

    def get_diagnosis(self, symptoms):
        # Call the Prolog knowledge base and return the diagnosis
        result = subprocess.run(['swipl', '-s', 'src/prolog/knowledge_base.pl', '-g', f'diagnose({symptoms}, Diagnosis)', '-t', 'halt'], 
                                capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else None

if __name__ == '__main__':
    unittest.main()