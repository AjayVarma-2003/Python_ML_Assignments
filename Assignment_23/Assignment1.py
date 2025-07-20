import pandas as pd

def main():
    Border = "-" * 50

    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82],
    }

    df = pd.DataFrame(data)

    print(Border)
    print("Dimension of dataset is : ", df.shape)
    print(Border)

    print(Border)
    print("Columns in dataframe are : ", df.columns)
    print(Border)

    print(Border)
    print("Data types of data of columns : ")
    print(df.dtypes)
    print(Border)

    print(Border)
    print("Data in dataframe is : ")
    print(df)
    print(Border)

if __name__ == "__main__":
    main()