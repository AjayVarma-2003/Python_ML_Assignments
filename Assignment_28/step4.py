# step 4 :- Train and test the data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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

def Predictor(df):
    # dividing data
    x = df.drop(columns = ['Class'])
    y = df['Class']

    # getting standard scalar values of x
    scaler = StandardScaler()
    x_scaler = scaler.fit_transform(x)

    X_train, X_test, Y_train, Y_test = train_test_split(x_scaler, y, test_size = 0.2, random_state = 42)

    # doing parameter tuning
    accuracy_scores = []
    k_range = range(1, 21)

    for k in k_range:
        # building model
        model = KNeighborsClassifier(n_neighbors = k)

        # train model
        model.fit(X_train, Y_train)

        # test model
        Y_predicted = model.predict(X_test)

        # calculating accuracy
        accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

        accuracy_scores.append(accuracy)

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]

    accuracy = accuracy_scores[best_k + 1]

    return accuracy, best_k

def WinePredictor(dataset):
    df = pd.read_csv(dataset)

    print("Datset loaded successfully ...")
    print("First 5 entries of data set is : ")
    print(df.head())

    CleanData(df)

    DataVisualization(df)

    accuracy, k = Predictor(df)

    print("Using K-nearest neighbour algorithm classifier for this case study.")

    print("Best value of k to get best accuracy is : ", k)

    print("Using the best value of k accuracy is : ",accuracy)

def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()