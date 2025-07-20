import pandas as pd
import numpy as np

def main():
    Border = "-" * 50

    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [np.nan, 90, 78],
        'Science' : [92, np.nan, 80],
    }

    df = pd.DataFrame(data)

    print(Border)
    print("Original dataframe is : ")
    print(df)
    print(Border)

    print(Border)
    print("Number of missing values in dataframe is : ")
    print(df.isnull().sum())
    print(Border)

    df['Math'] = df['Math'].fillna(df['Math'].mean())   # replacing missing values with mean value of column
    df['Science'] = df['Science'].fillna(df['Science'].mean())

    print(Border)
    print("Dataframe after handling missing values is : ")
    print(df)
    print(Border)

if __name__ == "__main__":
    main()