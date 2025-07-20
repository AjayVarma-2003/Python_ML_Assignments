import pandas as pd

def main():
    data = {'Salary' : [25000, 27000, 29000, 31000, 50000, 100000]}

    df = pd.DataFrame(data)

    # calculate firs quartile and third quartile
    q1 = df['Salary'].quantile(0.25)
    q3 = df['Salary'].quantile(0.75)

    IQR = q3 - q1

    lower = q1 - (1.5 * IQR)
    upper = q3 + (1.5 * IQR)

    outliers = df[(df['Salary'] < lower) | (df['Salary']) > upper]

    print("Outliers of dataframe are : ", outliers)

if __name__ == "__main__":
    main()