# step 3 :- Train and test the model 

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def CleanData(df):
    # dropping unnecessary column
    df = df.drop(columns = 'Unnamed: 0', axis = 1)
    
    # encoding dependent and independent variable column
    df['Whether'] = df['Whether'].map({'Sunny' : 0, 'Overcast' : 1, 'Rainy' : 2})
    df['Temperature'] = df['Temperature'].map({'Hot' : 0, 'Mild' : 1, 'Cool' : 2})
    df['Play'] = df['Play'].map({'No' : 0, 'Yes' : 1})

    return df

def Predictor(df):
    # dividing data into train data and test data
    x = df[['Whether', 'Temperature']]
    y = df['Play']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    # model building
    model = LogisticRegression()

    # train model
    model.fit(X_train, Y_train)

    # test model
    Y_predicted = model.predict(X_test)

    # Calculating accuracy of model
    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    # Displaying confusion matrix
    con_matrix = confusion_matrix(Y_test, Y_predicted)

    return accuracy, con_matrix

def PlayPredictor(Dataset):
    df = pd.read_csv(Dataset)

    print("Dataset loaded successfully...")
    print("Firsr 5 entries of dataset are : ")
    print(df.head())

    df = CleanData(df)
    print("Dataset after step 2 :")
    print(df.head())

    accuracy, con_matrix = Predictor(df)

    print("Accuracy of model is : ", accuracy)
    print("Confusion matrix is : ")
    print(con_matrix)

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()