import pandas as pd
import numpy as np

def CleanData(df):
    # No need of column CodeNumber
    df.drop(columns = "CodeNumber", axis = 1, inplace = True)

    # Checking for missing values and if there are any then handle is
    print("Number of missing values in dataset are : ")
    print(df.isnull().sum())

    # handling ? data
    df['BareNuclei'] = df['BareNuclei'].replace('?', np.nan)
    df = df.replace(np.nan, 0)

    return df

def BreastCancerPredictor(dataset):
    df = pd.read_csv(dataset)

    print("First 5 entries of dataset is : ")
    print(df.head())

    print("Dimension of dataset is : ", df.shape)

    df= CleanData(df)
    print("Dataset dimension after handling unnecessary dataset columns : ", df.shape)

def main():
    BreastCancerPredictor("breast-cancer-wisconsin.csv")

if __name__ == "__main__":
    main()