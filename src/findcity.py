import pandas as pd
link = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"

# find the column name of the tables
tables = pd.read_html(link,header=0)

# pick one table to retrieve columns names 
table = tables[2]
column_names = table.columns

# concat the tables
df = pd.DataFrame(columns=column_names)

for table in tables:
    df = pd.concat([df, table])

# Get the language and city column
languages = df.iloc[:, 4]
cities = df.iloc[:, 1]

# get the country column (first column)
countries = df.iloc[:, 0]

df1 = pd.DataFrame({
    "Country":countries,
    "Language":languages,
    "City":cities
})

# save the results to csv file locally
df1.to_csv("cityNames.csv", index=False)
# print(df1.shape)
print("You got all the cities saved locally!!")