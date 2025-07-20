import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {
        'Age' : [22, 25, 47, 52, 46, 56],
        'Purchased' : [0, 1, 1, 0, 1, 0],
    }

    df = pd.DataFrame(data)

    print("Dimensions of data set is : ")
    print(df.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(df['Age'], df['Purchased'], test_size = 0.2)

    print("Dimension of X_train is : ", X_train.shape)
    print("Dimension of X_test is : ", X_test.shape)
    print("Dimension of Y_train is : ", Y_train.shape)
    print("Dimension of Y_test is : ", Y_test.shape)

if __name__ == "__main__":
    main()