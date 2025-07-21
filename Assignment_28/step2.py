# step 2 :- Clean, prepare and manipulate data

import pandas as pd

def CleanData(df):
    # no need to drop any column now.
    # checking for missing values and remove if they are present
    print("Number of missing values in dataset")
    print(df.isnull().sum())

def WinePredictor(dataset):
    df = pd.read_csv(dataset)

    print("Datset loaded successfully ...")
    print("First 5 entries of data set is : ")
    print(df.head())

    CleanData(df)

def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()