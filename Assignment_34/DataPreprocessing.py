import pandas as pd
from sklearn.preprocessing import normalize

def DataPreprocessing(df):
    # Checking if there any missing data
    print("Number of missing values in data are : ")
    print(df.isnull().sum())

    # Deleting column id as it is not necessary here
    df.drop(columns = ['id'], axis = 1, inplace = True)

    # encoding diagnosis column
    df['diagnosis'] = df['diagnosis'].map({'M' : 0, 'B' : 1})

    # normalizing data
    normalize(df, norm = "l1")

    return df
    
def BreastCancerPredictor(dataset):
    df = pd.read_csv(dataset)

    print("First 5 entries of dataset are : ")
    print(df.head())

    df = DataPreprocessing(df)

def main():
    BreastCancerPredictor("breast-cancer.csv")

if __name__ == "__main__":
    main()