# step 1 :- Load data

import pandas as pd

def WinePredictor(dataset):
    df = pd.read_csv(dataset)

    print("Datset loaded successfully ...")
    print("First 5 entries of data set is : ")
    print(df.head())

    print("Statistical summary is : ")
    print(df.describe())

def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()