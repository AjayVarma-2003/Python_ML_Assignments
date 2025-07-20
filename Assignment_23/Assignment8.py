import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Border = "-" * 50

    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82],
    }

    df = pd.DataFrame(data)

    col_names = df.columns

    x = []
    for i in range(1, len(col_names)):
        x.append(col_names[i])

    y = df[df['Name'] == 'Amit'].iloc[0, 1:].values    # it will store 85, 92, 75.

    plt.plot(x, y)
    plt.xlabel("Subjects")
    plt.ylabel("Amit's marks")
    plt.title("Line Chart")
    plt.show()
    
if __name__ == "__main__":
    main()

# iloc[0, 1:].values = iloc is integer location based indexing. 0 -> First row, 1: -> All columns excluding name, 
# .values -> it will only store the values of keys.