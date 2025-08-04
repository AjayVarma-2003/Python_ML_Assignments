import pandas as pd

def BreastCancerPredictor(dataset):
    df = pd.read_csv(dataset)

    print("First 5 entries of dataset are : ")
    print(df.head())

def main():
    BreastCancerPredictor("breast-cancer.csv")

if __name__ == "__main__":
    main()