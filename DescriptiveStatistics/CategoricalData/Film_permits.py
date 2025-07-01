import pandas as pd
import numpy as np

# Read CSV
film_permits = pd.read_csv('film_permits.csv')

# Looking at the first few rows
print(film_permits.head())

#Nominal variables
nominal = ["EventType", "Category", "SubCategoryName", "Borough"]

# Ordinal Vars - We might consider an Id like 'EventID' an ordinal variable in some situations

#Boroughs with most theatre permits
theater = film_permits[film_permits["SubCategoryName"] == "Theater"]
print(theater)
print(theater["Borough"].value_counts())

#Boroughs with most pilot permits
pilots = film_permits[film_permits["SubCategoryName"] == "Pilot"]
print(pilots)
print(pilots["Borough"].value_counts())

#Summarize the types: Category and SubCategoryName
print(film_permits["Category"].value_counts())

print(film_permits["SubCategoryName"].value_counts())
