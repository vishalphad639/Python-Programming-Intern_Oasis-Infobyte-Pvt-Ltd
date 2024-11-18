import pandas as pd
import matplotlib.pyplot as plt

def plot_bmi_trend(name):
    df = pd.read_csv("bmi_data.csv")
    user_data = df[df["Name"] == name]
    
    if user_data.empty:
        print("No data found for user.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(user_data["BMI"], marker='o')
    plt.title(f'BMI Trend for {name}')
    plt.xlabel('Record Number')
    plt.ylabel('BMI')
    plt.xticks(range(len(user_data)), range(1, len(user_data) + 1))
    plt.grid()
    plt.show()
