# step 3 :- Data visualizaion

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def CleanData(df):
    # no need to drop any column now.
    # checking for missing values and remove if they are present
    print("Number of missing values in dataset")
    print(df.isnull().sum())

def DataVisualization(df):
    plt.figure(figsize = (10, 8))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Correlational heatmap")
    plt.show()

def WinePredictor(dataset):
    df = pd.read_csv(dataset)

    print("Datset loaded successfully ...")
    print("First 5 entries of data set is : ")
    print(df.head())

    CleanData(df)

    DataVisualization(df)

def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()