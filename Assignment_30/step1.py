# Step 1 - Load data

import pandas as pd

def BankPredicctor(dataset):
    df = pd.read_csv(dataset, sep = ";")

    print("First 5 entries of dataset are : ")
    print(df.head())

def main():
    BankPredicctor("bank-full.csv")

if __name__ == "__main__":
    main()