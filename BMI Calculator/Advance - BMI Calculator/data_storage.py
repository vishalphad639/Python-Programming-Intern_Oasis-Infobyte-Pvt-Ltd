import pandas as pd
import os

DATA_FILE = "bmi_data.csv"

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Name", "Weight", "Height", "BMI", "Category"])

def save_data(name, weight, height, bmi, category):
    df = load_data()
    new_data = pd.DataFrame([[name, weight, height, bmi, category]], columns=["Name", "Weight", "Height", "BMI", "Category"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def get_user_data(name):
    df = load_data()
    return df[df["Name"] == name]
