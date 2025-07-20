import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("Output.csv")

    x = df['Name']
    y = df['Math']

    plt.hist(y, bins = 6, color = 'blue', edgecolor = 'black')
    plt.xlabel("Name of students")
    plt.ylabel("Marks in maths")
    plt.title("Math marks of students")
    plt.show()

if __name__ == "__main__":
    main()