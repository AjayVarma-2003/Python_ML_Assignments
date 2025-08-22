# Step 2 - Process data

import pandas as pd

def DataPreprocessing(df):
    # checking for missing values any
    print("Missing values in dataset are : ")
    print(df.isnull().sum())
    # No missing values in dataset

    # dropping unuseful column
    df = df.drop(columns = "day", axis = 1)

    # encoding
    df["job"] = df["job"].map({"admin.": 0, "blue-collar": 1, "entrepreneur": 2, "housemaid": 3, "management": 4, "retired": 5,
                                "self-employed": 6, "services": 7, "student": 8, "technician": 9, "unemployed": 10, "unknown": 11})

    df["marital"] = df["marital"].map({"married": 0, "single": 1, "divorced": 2})

    df["education"] = df["education"].map({"primary": 0, "secondary": 1, "tertiary": 2, "unknown": 3})

    df["default"] = df["default"].map({"yes": 1, "no": 0})
    
    df["housing"] = df["housing"].map({"yes": 1, "no": 0})
    
    df["loan"] = df["loan"].map({"yes": 1, "no": 0})

    df["contact"] = df["contact"].map({"unknown": 0, "telephone": 1, "cellular": 2})

    df["poutcome"] = df["poutcome"].map({"failure": 0, "other": 1, "success": 2, "unknown": 3})

    df["month"] = df["month"].map({"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10,
                                    "nov": 11, "dec": 12})
    
    df["y"] = df["y"].map({ "no" : 0, "yes" : 1})

    return df

def BankPredicctor(dataset):
    df = pd.read_csv(dataset, sep = ";")

    print("First 5 entries of dataset are : ")
    print(df.head())

    df = DataPreprocessing(df)
    
    print("Dataset after data preprocessing : ")
    print(df.head())

def main():
    BankPredicctor("bank-full.csv")

if __name__ == "__main__":
    main()