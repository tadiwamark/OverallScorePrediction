import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'joblib'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'xgboost'])

import joblib
import pickle


def predict(
    joined,
    power_jumping,
    power_stamping,
    passing,
    team_jersey_number,
    defending,
    shooting,
    attacking_heading_accuracy,
    height_cm,
    age,
):
    #model = joblib.load(r"XGBoost.pkl")
    pickle_in = open('XGBoost.pkl', 'rb')
    classifier = pickle.load(pickle_in)
    
    test_data = [[
        joined,
        power_jumping,
        power_stamping,
        passing,
        team_jersey_number,
        defending,
        shooting,
        attacking_heading_accuracy,
        height_cm,
        age,
    ]]

    pred = classifier.predict(test_data)
    return pred


predict(45, 25, 12, 25, 12, 12, 15, 25, 25, 12)
