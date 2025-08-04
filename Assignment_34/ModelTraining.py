import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score, recall_score

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

def ExploratoryDataAnalysis(df):
    # Statistical summary of data
    print("Statistical summary of data is : ")
    print(df.describe())

    # Checking feature correlation
    # plt.figure(figsize = (12, 10))
    # sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    # plt.title("Feature correlation")
    # plt.show()

def Predictor(df):
    # dividing data
    x = df.drop(columns = 'diagnosis', axis = 1)
    y = df['diagnosis']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = LogisticRegression()

    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    conf_mat = confusion_matrix(Y_test, Y_predicted)

    precision = (precision_score(Y_test, Y_predicted)) * 100

    Recall = (recall_score(Y_test, Y_predicted)) * 100

    F1 = (f1_score(Y_test, Y_predicted)) * 100

    return accuracy, conf_mat, precision, Recall, F1
    
def BreastCancerPredictor(dataset):
    df = pd.read_csv(dataset)

    print("First 5 entries of dataset are : ")
    print(df.head())

    df = DataPreprocessing(df)

    ExploratoryDataAnalysis(df)

    accuracy, conf_mat, precision, Recall, F1 = Predictor(df)

    print("Accuracy of model is : ", accuracy)

    print("Confusion matrix is : ")
    print(conf_mat)

    print("Precision score is : ", precision)

    print("Recall score is : ", Recall)

    print("F1 score is : ", F1)

def main():
    BreastCancerPredictor("breast-cancer.csv")

if __name__ == "__main__":
    main()