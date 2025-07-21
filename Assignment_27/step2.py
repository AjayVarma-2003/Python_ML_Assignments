# step 2 :- Clean, prepare and manipulate data

import pandas as pd

def CleanData(df):
    # Dropping unnecessary columns
    df = df.drop(columns = 'Unnamed: 0', axis = 1)

    return df

def AdvertisingPredictor(dataset):
    df = pd.read_csv(dataset)

    print("Data set loaded successfully ...")
    print("First 5 entries of dataset : ")
    print(df.head())

    df = CleanData(df)
    print("Dataset after cleaning : ")
    print(df.head())

def main():
    AdvertisingPredictor("Advertising.csv")

if __name__ == "__main__":
    main()