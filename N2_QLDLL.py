import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Desktop\N2-QLDL.csv")

filter_data = df.iloc[: , [3,4]].values

with open("C:\\Users\\HP\Desktop\\K-means-data.txt", 'a') as f:
    for row in filter_data:
        f.write(f"{row[0]},{row[1]}\n")

print("successful")