import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def PreDataVisualization(df):
    plt.figure(figsize = (10, 8))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.show()

def Diabetes(Dataset):
    df = pd.read_csv(Dataset)

    print("First 5 entries of dataset are : ")
    print(df.head())

    print("Statistical summary of dataset is : ")
    print(df.describe())

    PreDataVisualization(df)

def main():
    Diabetes("diabetes.csv")

if __name__ == "__main__":
    main()