import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D plotting

def CleanData(df):
    # removing unnecessary columns
    df = df.drop(columns = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian",
                            "traveltime", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic", "famrel",
                            "freetime", "goout", "Dalc", "Walc", "health"], axis = 1)
    
    return df

def ClusteringAndVisualize(df):
    df = df.select_dtypes(include = ["int64", "float64"])

    # Standardising data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Kmeans model
    kmeans = KMeans(n_clusters = 3, random_state = 42, n_init = 10)
    df["clusters"] = kmeans.fit_predict(scaled_data)

    # Mapping clusters to categories
    cluster_means = df.groupby("clusters")["G3"].mean().sort_values()
    mapping = {cluster_means.index[0] : "Struggiling Students",
               cluster_means.index[1] : "Average Performance students",
               cluster_means.index[2] : "Top performance students"}
    
    df["PerformanceCategory"] = df["Cluster"].map(mapping)

    print("Cluster Counts : ")
    print(df["PerformanceCategory"].value_counts())

    # Cluster graph
    fig = plt.figure(figsize = (10, 8))
    ax = fig.add_subplot(111, projection = "3d")

    scatter = ax.scatter(df["G1"], df["G2"], df["G3"], 
                         c=df["Cluster"], cmap="viridis", s=60)

    # Centroids (inverse transform to original scale)
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    ax.scatter(centroids[:, df.columns.get_loc("G1")], 
               centroids[:, df.columns.get_loc("G2")], 
               centroids[:, df.columns.get_loc("G3")], 
               s=300, marker="X", c="red", edgecolor="black", label="Centroids")

    ax.set_title("3D Cluster Visualization (G1 vs G2 vs G3)")
    ax.set_xlabel("G1 Score")
    ax.set_ylabel("G2 Score")
    ax.set_zlabel("G3 Score")
    ax.legend()
    plt.show()

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

    ClusteringAndVisualize(df)

def main():
    StudentPerformancePredictor("student-mat.csv")

if __name__ == "__main__":
    main()