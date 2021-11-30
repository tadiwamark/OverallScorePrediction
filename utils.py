import joblib


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
    model = joblib.load(r"https://github.com/tadiwamark/OverallScorePrediction/blob/main/XGBoost.pkl")

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
    pred = model.predict(test_data)
    return pred


predict(45, 25, 12, 25, 12, 12, 15, 25, 25, 12)
