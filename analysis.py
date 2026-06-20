from data_loading import *
from data_preprocessing import *

# Total Number of Respondents

total_respondents = df['ResponseId'].nunique()
print(f'Total number of respondents who participated in the survey: 'f'{total_respondents}')



# Response Completeness Analysis

schema_questions = set(df1['qname'].unique())
df_columns = set(df.columns)

questions = list(schema_questions.intersection(df_columns))
respondents_all_answered = (df.dropna(subset=questions).shape[0])

print(f'Number of questions checked: {len(questions)}')
print(f'Number of respondents who answered all questions: 'f'{respondents_all_answered}')



# Statistical Analysis of Respondents' Experience

print('Measures of central tendency:')
print(f"Mean: " f"{round(df['WorkExp'].mean(skipna=True), 1)}")
print(f"Median: " f"{df['WorkExp'].dropna().median()}")
print(f"Mode: " f"{df['WorkExp'].dropna().mode()}")



# Remote Work Analysis

remote_workers = df[df['RemoteWork'] == 'Remote']
print(f'Number of respondents working remotely: 'f'{remote_workers.shape[0]}')



# Python Popularity Analysis

python_users_count = (df['worked_with_python'].sum())
python_percent = round((python_users_count / total_respondents) * 100,2)
print(f'Percentage of respondents who have worked with Python: 'f'{python_percent}%')



# Analysis of Programming Learning Paths

online_courses_count = (df['learned_with_online_courses'].sum())
print(f'Total number of respondents who selected online courses: 'f'{online_courses_count}')


# Compensation Analysis of Python Developers by Country

py_progers_by_country = (python_df.groupby('Country')['ConvertedCompYearly'].agg(['mean', 'median']))
py_progers_by_country.columns = ['Mean','Median']
py_progers_by_country.head(10)


# Education Analysis of Top-Paid Specialists

top_5_specialists = (top_paid.sort_values(by='ConvertedCompYearly',ascending=False).reset_index(drop=True).head(5))
top_5_specialists

# Industry Analysis of High-Paid Remote Workers

print('Most common industries among highly paid remote workers:')
top_industries = (high_earn_remote['Industry'].value_counts())
top_industries
