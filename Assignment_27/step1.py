# step 1 :- Load data

import pandas as pd

def AdvertisingPredictor(dataset):
    df = pd.read_csv(dataset)

    print("Data set loaded successfully ...")
    print("First 5 entries of dataset : ")
    print(df.head())

    print("Statistical summary is : ")
    print(df.describe())

def main():
    AdvertisingPredictor("Advertising.csv")

if __name__ == "__main__":
    main()