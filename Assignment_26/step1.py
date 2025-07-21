# step 1 :- load data

import pandas as pd

def PlayPredictor(Dataset):
    df = pd.read_csv(Dataset)

    print("Dataset loaded successfully...")
    print("Firsr 5 entries of dataset are : ")
    print(df.head())

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()