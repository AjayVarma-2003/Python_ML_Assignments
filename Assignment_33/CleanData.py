import pandas as pd

def CleanData(df):
    # removing unnecessary columns
    df = df.drop(columns = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian",
                            "traveltime", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic", "famrel",
                            "freetime", "goout", "Dalc", "Walc", "health"], axis = 1)
    
    return df

def StudentPerformancePredictor(dataset):
    # Read the raw file as plain text
    with open("student-mat.csv", "r") as f:
        lines = f.readlines()

    # Fix header
    header = lines[0].strip().replace('"', '').split(',')

    # Write a cleaned file
    with open("student-mat-clean.csv", "w") as f:
        f.write(";".join(header) + "\n")
        for line in lines[1:]:
            cleaned = line.strip().strip('"')   # remove outer quotes
            cleaned = cleaned.replace('""', '') # remove leftover double quotes inside
            cleaned = cleaned.replace(',', ';') # ensure separators are ';'
            f.write(cleaned + "\n")

    # Load with pandas
    df = pd.read_csv("student-mat-clean.csv", sep=";")

    # Clean up numeric columns that still look messy
    for col in ["G1","G2","G3"]:
        df[col] = df[col].astype(str).str.extract(r'(\d+)')  # keep only digits
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print("First 5 entries of dataset is : ")
    print(df.head())

    df = CleanData(df)

    print("Dataset dimension after data cleaning is : ", df.shape)

def main():
    StudentPerformancePredictor("student-mat.csv")

if __name__ == "__main__":
    main()