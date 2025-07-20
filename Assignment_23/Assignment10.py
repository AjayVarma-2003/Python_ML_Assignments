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
    print("Original dataframe is : ")
    print(df)
    print(Border)

    df = df.drop('English', axis = 1)

    print(Border)
    print("Dataframe after dropping column english : ")
    print(df)
    print(Border)

if __name__ == "__main__":
    main()