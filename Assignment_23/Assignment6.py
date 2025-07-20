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

    df['Total'] = df['Math'] + df['Science'] + df['English']

    df = df.sort_values('Total', ascending = False)

    print("Dataset after adding new column 'Total' and printing in descending order : ")
    print(df)

    print(Border)

if __name__ == "__main__":
    main()