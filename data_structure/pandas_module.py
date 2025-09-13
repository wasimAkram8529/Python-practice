import pandas as ps
import sys


df = ps.read_csv("/home/wasim/python_dir/data_structure/employees.csv")
print(df)
# sorted_df = df.sort_values(by=["Age", "ID"], ascending=False)
# print(sorted_df)
# print(df.info())
# print(df.describe())
# print(df.columns)

# filtered_df = df[df['Age'] > 30]
# print(filtered_df)

# it_employees = df[df['Department'] == 'IT']
# print(it_employees)

# aggregated_data = df.groupby("Department")["Salary"].mean()
# print(aggregated_data)

# aggregated_data_2 = df.groupby("Department")["ID"].count()
# print(aggregated_data_2)

# aggregated_data_3 = df.groupby("Department")["Salary"].max()
# print(aggregated_data_3)

# df['Bonus'] = df['Salary'] * 0.10
# print(df)
# df["Seniority"] = df['Age'].apply(lambda age: "Senior" if age > 35 else "Junior")
# print(df)

# df["JoiningDate"] = ps.to_datetime(df["Joining_Date"])
# df['JoiningYear'] = df['JoiningDate'].dt.year
# print(df[["Name", "JoiningDate", "JoiningYear"]])
print(df.isnull().sum())
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)

index = df[df['Salary'] > 50000].index
print(index)
print(df.query("Age > 30"))