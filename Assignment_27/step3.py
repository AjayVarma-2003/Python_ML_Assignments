# step 3 :- data visualization with figures

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def CleanData(df):
    # Dropping unnecessary columns
    df = df.drop(columns = 'Unnamed: 0', axis = 1)

    return df

def DataVisualization(df):
    plt.figure(figsize = (10, 8))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Correlational heatmap of independent and dependent variable")
    plt.show()

def AdvertisingPredictor(dataset):
    df = pd.read_csv(dataset)

    print("Data set loaded successfully ...")
    print("First 5 entries of dataset : ")
    print(df.head())

    df = CleanData(df)
    print("Dataset after cleaning : ")
    print(df.head())

    DataVisualization(df)

def main():
    AdvertisingPredictor("Advertising.csv")

if __name__ == "__main__":
    main()