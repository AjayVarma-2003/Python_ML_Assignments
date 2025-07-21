# step 4 :- Train and test model.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error

def CleanData(df):
    # Dropping unnecessary columns
    df = df.drop(columns = 'Unnamed: 0', axis = 1)

    return df

def DataVisualization(df):
    # data visualizing using correlation heatmap
    plt.figure(figsize = (10, 8))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Correlational heatmap of independent and dependent variable")
    plt.show()

def Predictor(df):
    # dividing data
    x = df[['TV', 'radio', 'newspaper']]
    y = df['sales']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    # building model
    model = LinearRegression()

    # train model
    model.fit(X_train, Y_train)

    # test model
    Y_predicted = model.predict(X_test)

    # calculating accuracy of model
    r2 = r2_score(Y_test, Y_predicted)

    MSE = mean_squared_error(Y_test, Y_predicted)

    RMSE = root_mean_squared_error(Y_test, Y_predicted)

    return r2, MSE, RMSE

def AdvertisingPredictor(dataset):
    df = pd.read_csv(dataset)

    print("Data set loaded successfully ...")
    print("First 5 entries of dataset : ")
    print(df.head())

    df = CleanData(df)
    print("Dataset after cleaning : ")
    print(df.head())

    DataVisualization(df)

    r2, MSE, RMSE = Predictor(df)

    print("R-square value is : ", r2)
    print("Mean squared error value is : ", MSE)
    print("Root mean squared error value is : ", RMSE)

def main():
    AdvertisingPredictor("Advertising.csv")

if __name__ == "__main__":
    main()