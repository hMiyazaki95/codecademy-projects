
'''
Analyzing Data with Pandas
3 min
Catherine wants to know if Codecademy learners are finding what they need. She needs to analyze data from a survey that was administered to a subset of visitors.

Catherine selects the survey data from the SQL database and downloads it onto her computer. She saves the data as a CSV file (extension .csv), which stands for Comma-Separated Values. CSV is a text-only spreadsheet format that lets us store and explore data.

To analyze the survey data, Catherine will use pandas. Python is a programming language, and pandas is a special set of commands in Python that lets us analyze spreadsheet data. Pandas can do a lot of the things that SQL can do, but it’s also backed by the power of Python, so we can easily transition from analyzing our data with pandas to visualizing it using other Python tools.
'''

import codecademylib3_seaborn

# Paste code here:
import pandas as pd

# Load data
df = pd.read_csv('page_visits.csv')

# Display data
print(df.head())