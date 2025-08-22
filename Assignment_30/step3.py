# Step 2 - Process data

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def DataPreprocessing(df):
    # dropping unuseful column
    df = df.drop(columns = ["day", "month"], axis = 1)

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

    # df["month"] = df["month"].map({"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10,
    #                                 "nov": 11, "dec": 12})
    
    df["y"] = df["y"].map({ "no" : 0, "yes" : 1})

    return df

def Predictor(df):
    x = df.drop(columns = "y", axis = 1)
    y = df["y"]

    # split training and testing data
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = LogisticRegression(max_iter = 1000)

    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    conf_mat = confusion_matrix(Y_test, Y_predicted)

    return accuracy, conf_mat  

def BankPredicctor(dataset):
    df = pd.read_csv(dataset, sep = ";")

    print("First 5 entries of dataset are : ")
    print(df.head())

    df = DataPreprocessing(df)
    
    print("Dataset after data preprocessing : ")
    print(df.head())

    accuracy, conf_mat = Predictor(df)

    print("Accuracy is : ", accuracy)
    # using month column accuracy is : 88.19
    # without using month columns accuracy is : 88.45

    print("Confusion matrix is : ")
    print(conf_mat)

def main():
    BankPredicctor("bank-full.csv")

if __name__ == "__main__":
    main()