import pandas as pd

def BreastCancerPredictor(dataset):
    df = pd.read_csv(dataset)

    print("First 5 entries of dataset is : ")
    print(df.head())

    print("Statistical information of dataset is : ")
    print(df.describe())

def main():
    BreastCancerPredictor("breast-cancer-wisconsin.csv")

if __name__ == "__main__":
    main()