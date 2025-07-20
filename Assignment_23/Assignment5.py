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

    df.replace({'Name' : 'Pooja'}, 'Puja', inplace = True)    # df.method({col : value1}, value2, inplace = True)

    print(Border)
    print("Data after updation : ")
    print(df)
    print(Border)

if __name__ == "__main__":
    main()