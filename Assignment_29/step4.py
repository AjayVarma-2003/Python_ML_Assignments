import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def PreDataVisualization(df):
    plt.figure(figsize = (10, 8))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.show()

def CleanData(df):
    print("Number of missing values in dataset is : ")
    print(df.isnull().sum())

    return df

def Predictor(x, y):
    # taking standard scaler value of x
    scaler = StandardScaler()
    x_scaler = scaler.fit_transform(x)

    X_train, X_test, Y_train, Y_test = train_test_split(x_scaler, y, test_size = 0.2, random_state = 42)

    model = LogisticRegression()
    
    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    matrix = confusion_matrix(Y_test, Y_predicted)

    report = classification_report(Y_test, Y_predicted)

    return accuracy, matrix, report

def PostDataVisualization(matrix):
    plt.figure(figsize = (10, 8))
    sns.heatmap(matrix, annot = True, cmap = 'coolwarm')
    plt.show()

def Diabetes(Dataset):
    df = pd.read_csv(Dataset)

    print("First 5 entries of dataset are : ")
    print(df.head())

    PreDataVisualization(df)

    df = CleanData(df)

    x = df.drop(columns = 'Outcome', axis = 1)
    y = df['Outcome']

    accuracy, con_matrix, report = Predictor(x, y)

    print("Accuracy of model is : ", accuracy)

    print("Confusion matrix is : ")
    print(con_matrix)

    print("Classification report of model is : ")
    print(report)

    PostDataVisualization(con_matrix)
    
def main():
    Diabetes("diabetes.csv")

if __name__ == "__main__":
    main()