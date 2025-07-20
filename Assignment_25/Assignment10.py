import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {
        'Age' : [25, 30, 45, 35, 22],
        'Salary' : [50000, 60000, 80000, 65000, 45000],
        'Purchased' : [1, 0, 1, 0, 1],
    }

    df = pd.DataFrame(data)

    x = df[['Age', 'Salary']]
    y = df['Purchased']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2)

    print("Dimension of X_train is : ", X_train.shape)
    print("Dimension of Y_train is : ", Y_train.shape)
    print("Dimension of X_test is : ", X_test.shape)
    print("Dimension of Y_test is : ", Y_test.shape)

if __name__ == "__main__":
    main()