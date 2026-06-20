# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gdow

file_id = '1sWvTthFAMt2Hn-9hpO4MebnbtiOVDnsB'
schema_id = '1DqogmP4X7iStjzZpAhuMeRxNXjiZq1p3'

url = f'https://drive.google.com/uc?id={file_id}'
url1 = f'https://drive.google.com/uc?id={schema_id}'

# Download the survey file
output = 'survey_results.csv'
gdown.download(url, output, quiet=False)

# Read CSV files using UTF-8 encoding
df = pd.read_csv(output, encoding='utf-8')
df1 = pd.read_csv(url1, encoding='utf-8')

# Display all columns in the DataFrame
pd.set_option('display.max_columns', None)

df.head(10)
df1
