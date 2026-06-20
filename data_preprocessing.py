# Create a new column that contains True/False
df['worked_with_python'] = (
    df['LanguageHaveWorkedWith']
    .str.contains('Python', na=False)
)

# Create a new column that contains True/False
df['learned_with_online_courses'] = (
    df['LearnCode']
    .str.contains('Online Courses', na=False)
)

# Filter respondents who have worked with Python
python_df = df[
    (df['worked_with_python'] == True)
]

# Keep only records with salary information
python_df = python_df[
    python_df['ConvertedCompYearly'].notna()
]

# Calculate the third quartile (75th percentile)
third_quartile_salary = (
    df['ConvertedCompYearly']
    .quantile(0.75)
)

# Respondents above the 75th percentile
# who also work remotely
high_earn_remote = (
    df[
        (df['ConvertedCompYearly'] > third_quartile_salary)
        &
        (df['RemoteWork'] == 'Remote')
    ]
    .reset_index(drop=True)
)
