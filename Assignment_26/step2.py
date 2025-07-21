# step 2:- Clean, Prepare and manipulate data

import pandas as pd

def CleanData(df):
    # dropping unnecessary column
    df = df.drop(columns = 'Unnamed: 0', axis = 1)
    
    # encoding dependent and independent variable column
    df['Whether'] = df['Whether'].map({'Sunny' : 0, 'Overcast' : 1, 'Rainy' : 2})
    df['Temperature'] = df['Temperature'].map({'Hot' : 0, 'Mild' : 1, 'Cool' : 2})
    df['Play'] = df['Play'].map({'No' : 0, 'Yes' : 1})

    return df

def PlayPredictor(Dataset):
    df = pd.read_csv(Dataset)

    print("Dataset loaded successfully...")
    print("Firsr 5 entries of dataset are : ")
    print(df.head())

    df = CleanData(df)
    print("Dataset after step 2 :")
    print(df.head())

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()