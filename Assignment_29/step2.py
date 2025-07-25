import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def PreDataVisualization(df):
    plt.figure(figsize = (10, 8))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.show()

def CleanData(df):
    print("Number of missing values in dataset is : ")
    print(df.isnull().sum())
    # no missing values
    # all columns are important factors in detecting diabetes.

    return df

def Diabetes(Dataset):
    df = pd.read_csv(Dataset)

    print("First 5 entries of dataset are : ")
    print(df.head())

    PreDataVisualization(df)

    df = CleanData(df)

    # splitting data into features and targets
    x = df.drop(columns = 'Outcome', axis = 1)
    y = df['Outcome']
    
def main():
    Diabetes("diabetes.csv")

if __name__ == "__main__":
    main()