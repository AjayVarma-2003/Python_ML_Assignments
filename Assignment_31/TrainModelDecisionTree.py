import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def CleanData(df):
    # No need of column CodeNumber
    df.drop(columns = "CodeNumber", axis = 1, inplace = True)

    # Checking for missing values and if there are any then handle is
    print("Number of missing values in dataset are : ")
    print(df.isnull().sum())

    # handling ? data and replacing it with 0
    df['BareNuclei'] = df['BareNuclei'].replace('?', np.nan)
    df = df.replace(np.nan, 0) 

    return df

def PredictorDecisionTree(df):
    # Checking the accuracy using decision tree classifier.

    # divide data into labels and target
    x = df.drop(columns = 'CancerType', axis = 1)
    y = df['CancerType']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2 , random_state = 42)
    
    # model building
    model = DecisionTreeClassifier()

    # model training
    model.fit(X_train, Y_train)

    # model testing and calculating accuracy
    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    conf_mat = confusion_matrix(Y_test, Y_predicted)

    return accuracy, conf_mat

def BreastCancerPredictor(dataset):
    df = pd.read_csv(dataset)

    print("First 5 entries of dataset is : ")
    print(df.head())

    df= CleanData(df)

    accuracy , conf_mat = PredictorDecisionTree(df)
    print("Accuracy using Decision tree classifier is : ", accuracy)

    print("Confustion matrix of Decision tree classifier is : ")
    print(conf_mat)

def main():
    BreastCancerPredictor("breast-cancer-wisconsin.csv")

if __name__ == "__main__":
    main()