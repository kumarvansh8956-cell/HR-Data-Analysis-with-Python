import pandas as p
import numpy as n
import Read_and_exploration as r


df = r.read_Data("HR_Analytics.csv")

r.explorating(df)

'''
Checking for improper data

'''
r.Checking_data(df)

"""
Does not found any specific improperdata 

"""

print("checking for missing data")

print( df.isnull())

df = df.drop(columns='YearsWithCurrManager')


print("Column YearsWithCurrManager is removed")

print(" duplicate value are remove")

df.drop_duplicates(
  inplace= True
)
"""
Explanation:-

For this dataset we don't need this column 'YearsWithCurrManager'
"""
print("#"*30 + ' status of the dataframe'+ "#"*30 )
print(" for columns")
print(df.columns)
print(" For duplicate")
print(df.duplicated().sum())
print(" for datatype")
print(df.dtypes)



# Analysis Phase
print("="*30 + '| ANALYSIS PHASE |'+ "="* 30)
# How many employees are there?
print(" the total numbers of employeees")
print(df["EmpID"].count())
# How many columns and features are present?
Colu = df.columns.to_list()
print(f' The number of columns in dataset is {len(Colu)} and the feature is {len(Colu)-1} ')
# What is the data type of each column?
print(' the datatype of the columns is:-')
print(df.dtypes)
# What are the summary statistics of numerical columns?
print('the summary statistics odf the dataframe is')
print(df.describe())
# What unique values exist in categorical columns?
for col in df.columns:
  print(f" the unique value in the {col}")
  print(df[col].unique())

# What is the age distribution of employees?
A_d = df.groupby('AgeGroup')["EmpID"].count()
print(" the Age group in the data set is")
print(A_d)
# Which age group has the highest number of employees?
print(f' the highest number of employee is in {A_d.idxmax()} with {A_d.max()} members')
# Gender distribution of employees.
gender = df.groupby('Gender')['EmpID'].count()
print(" the gender ratios")
print(gender)
# Marital status distribution.
Relation = df.groupby('MaritalStatus')['EmpID'].count()
print(Relation)
# Education level distribution.
education_map = {
    1: "Below College",
    2: "College",
    3: "Bachelor",
    4: "Master",
    5: "Doctor"
}

df["Education"] = df["Education"].map(education_map)
Study =  df.groupby('Education')['EmpID'].count()
print(Study)

# Which education field has the most employees?

Edu_Field =  df.groupby('EducationField')['EmpID'].count()
print(" the Education field of employee is ")
print(Edu_Field)
print(f'education field has the most employees is {Edu_Field.idxmax()} with total {Edu_Field.max()} employee')


# Which department has the most employees?

Depart =  df.groupby('Department')['EmpID'].count()

print(" Here the distribution by Department ")
print(Depart)
print(f'Department has the most employees is {Depart.idxmax()} with total {Depart.max()} employee')

# Which job role has the highest employee count?

Jobs =  df.groupby('JobRole')['EmpID'].count()
print(" Here the distribution by JobRole")
print(Jobs)
print(f' the job roles has the most employees is {Jobs.idxmax()} with total {Jobs.max()} employee')

# Distribution of employees across job levels.
print(" Here the distribution by jobLevel ")
Joblevels =  df.groupby('JobLevel')['EmpID'].count()
print(Joblevels)
# Average monthly income by department.

Avg_income_per_Month = df.groupby('Department')['MonthlyIncome'].mean()
print('The Average monthly income by department.')
print(Avg_income_per_Month)

# Average monthly income by job role.

Avg_income_per_Month_by_role = df.groupby('JobRole')['MonthlyIncome'].mean()
print('The Average monthly income by jobrole.')
print(Avg_income_per_Month_by_role)

# Highest-paying job role.

print(f"Highest-paying job role is {Avg_income_per_Month_by_role.idxmax()} with avrage income  { Avg_income_per_Month_by_role.max()} Rs ")
# Highest-paying department.

print(f"Highest-paying Department is {Avg_income_per_Month.idxmax()} with avrage income  { Avg_income_per_Month.max()} Rs ")


# Overall attrition rate.

employees_left = df[df['Attrition'] == "Yes"]
Attrition_Rate = (len(employees_left)/len(df))*100
print(f" the Attrition rate is {Attrition_Rate:.3f}%")

# How many employees stayed vs left?

employees_status = df.groupby("Attrition")['EmpID'].count()
print(" the Status of employee ")
print(employees_status)

# Which department has the highest attrition?
Attri_byDepo = employees_left.groupby('Department')['Attrition'].count()
print('Attrition by the department')
print(Attri_byDepo)

# Which job role experiences the highest attrition?

job_Attrit = employees_left.groupby("JobRole")['Attrition'].count()
print("job role experiences the highest attrition")
print(job_Attrit)

# Attrition by gender.

Gender_Attrit = employees_left.groupby("Gender")['Attrition'].count()
print('Attrition by the gender')
print(Gender_Attrit)

# Attrition by marital status.

Marital_Attri= employees_left.groupby('MaritalStatus')['Attrition'].count()
print('Attrition by the marital status')
print(Marital_Attri)


# Attrition by education level.

Edu_Attri= employees_left.groupby('Education')['Attrition'].count()
print('Attrition by the Education level')
print(Edu_Attri)

# Attrition by education field.

Edu_Field_Attri= employees_left.groupby('EducationField')['Attrition'].count()
print('Attrition by the Education field')
print(Edu_Field_Attri)

# Attrition by age group.

Agegroup_Attri= employees_left.groupby('AgeGroup')['Attrition'].count()
print('Attrition by the Age group')
print(Agegroup_Attri)


# Attrition by salary slab.

Salaryslab_Attri= employees_left.groupby('SalarySlab')['Attrition'].count()
print('Attrition by the salary slab')
print(Salaryslab_Attri)

# Monthly income distribution.


print(" The monthly income distribution ")
print(df['MonthlyIncome'].describe())

# Average salary by department.

Salary_by_depart = df.groupby('Department')['MonthlyIncome'].mean() 
print("Average salary by department")
print(Salary_by_depart)

# Average salary by job level.

JobLevel_map = {
    1: "Entry-level",
    2: "Experienced",
    3: "Senior",
    4: "Manager",
    5: "Executive/Director"
}

df['JobLevel'] = df['JobLevel'].map(JobLevel_map)


Salary_by_job_Level = df.groupby('JobLevel')['MonthlyIncome'].mean() 
print("Average salary by jobleve")
print(Salary_by_job_Level)


# Average salary by education.

Salary_by_education = df.groupby("Education")['MonthlyIncome'].mean() 
print("Average salary by jobleve")
print(Salary_by_education)

# Salary slab distribution.

print(df['SalarySlab'].describe())

# Do employees with lower salaries leave more often?

print(Salaryslab_Attri.sort_values(ascending= False))
"""
SalarySlab
Upto 5k    163
5k-10k      49
10k-15k     20
15k+         5 
 """
print(" Answer:--" + '\n' + " Yes, according to this dataset. The employees with salary below the 5000 usually left company more often then employees with higher salaries  ")



# Does overtime affect attrition?

print(" The effect of Overtime on the Attrition")
overtime_VS_Attriton = employees_left.groupby('OverTime')['Attrition'].count()
print(overtime_VS_Attriton)
"""
OverTime
No     110
Yes    127

"""
possiblility = (127/1470)*100

print(f"Yes, Over time employee has {possiblility: .3f}% more chance then non overtime employees ")

# Environment satisfaction vs attrition.

Attri_vs_Satis = employees_left.groupby("EnvironmentSatisfaction")["Attrition"].count()

print(" The effect of Environment satisfaction on the Attrition")
print(Attri_vs_Satis)
"""
Observation
Employee with least satisfaction have higher  chance for leaving 

"""

# Job satisfaction vs attrition.


Attri_vs_jSatis = employees_left.groupby("JobSatisfaction")["Attrition"].count()

print(" The effect of Job satisfaction on the Attrition")
print(Attri_vs_jSatis)
"""
Observation
Employee with least Job satisfaction have higher chance for leaving 

"""

# Work-life balance vs attrition.

Attri_vs_Worklife = employees_left.groupby('WorkLifeBalance')["Attrition"].count()

print(" The effect of Work-life balance on the Attrition")
print(Attri_vs_Worklife)

"""
WorkLifeBalance
1     25
2     58
3    127
4     27

"""
print(" The employee with good work-life balance leave more then others")

"""
Observation:-
The employees with good work-life balance leave more then others. maybe for maintaining better work life balance for healthy life and relaionship.  

"""

# Relationship satisfaction vs attrition.

Attri_vs_rSatis = employees_left.groupby('RelationshipSatisfaction')["Attrition"].count()

print(" The effect of Work-life balance on the Attrition")
print(Attri_vs_rSatis)

'''
Observation:-
employees with good or best relations leaving more then less.may be for maintaining a good relationship they switch the job maintaining for relationship and 
for supporting their life and relations. 

'''

# Job involvement vs attrition.

Attri_vs_jInvolve = employees_left.groupby('JobInvolvement')["Attrition"].count()

print(" The effect of relationship on the Attrition")
print(Attri_vs_jInvolve)

"""
JobInvolvement
1     28
2     71
3    125
4     13

"""
"""
Observation:-
employees with high involvement leaving more then less involvement

"""



# Total working years distribution.

Total_year = df.groupby('EmpID')['TotalWorkingYears'].sum()
print(Total_year)



# Years at company distribution.

print(df['YearsAtCompany'].value_counts().sort_index())

# Years in current role distribution.

print(df['YearsInCurrentRole'].value_counts().sort_index())

# Years since last promotion.

print(df['YearsSinceLastPromotion'].value_counts().sort_index())

# Number of companies worked before joining.

print(df['NumCompaniesWorked'].value_counts().sort_index())

# Average years at company by department.

avg_years = (
    df.groupby('Department')['YearsAtCompany']
      .mean()
      .sort_values(ascending=False)
)

print(avg_years)


# Correlation between numerical variables.

correl = df.corr(numeric_only= True)
print(correl)

# Which variables are most correlated with monthly income?

mon_inco_corr = correl["MonthlyIncome"]
print(mon_inco_corr)


# Which variables are strongly associated with attrition (after encoding)?
df["Attrition"] = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})
attrition_corr = (
    df.corr(numeric_only=True)["Attrition"]
    .drop("Attrition")
    .sort_values(ascending=False)
)

print(attrition_corr)
# Heatmap of numerical features.

correlation = df.corr(numeric_only=True)

# Which department should HR prioritize for retention?
"""
Department
Human Resources            12
Research & Development    133
Sales                      92

Observation:-
Research & Development is show higher attrition. HR should prioritize this department first.
"""
# Which employee group has the highest risk of leaving?
"""
The low-income salary group (~₹5,000) shows the highest attrition count (163), exceeding the maximum attrition observed in other employee
 categories such as Work-Life Balance, Job Satisfaction, and Relationship Satisfaction (maximum around 123-132).

"""
# Does overtime significantly increase attrition?
'''
Yes, Over time employee has  8.639% more chance then non overtime employees
'''
# Which salary slab requires attention?
'''
Employees earning up to ₹5K exhibit the highest attrition.
 HR should review compensation policies and career growth opportunities for this salary segment.

'''
# Which age group should receive retention programs?
"""
Answer 
the age group 55+ showing highest  retention
"""
# Which job roles need hiring due to high turnover?
"""
 Laboratory Technicians recorded the highest attrition count (62 employees). 
 HR should prioritize retention strategies and recruitment planning for this role to reduce turnover and maintain workforce stability.
"""
# Which satisfaction metric most influences attrition?
"""
Employees with low Environment Satisfaction (Level 1) show a relatively high number of attrition cases.
Job Satisfaction Level 3 records the highest attrition count within that category.
Relationship Satisfaction Level 3 also has a high attrition count.
The differences between these maximum counts are very small, so no single satisfaction metric clearly stands out as the strongest factor based on counts alone.

"""
# What are the top five reasons employees are likely leaving (based on the available data)?
"""
low income
high Job Involvement
Work Life Balance
high OverTime
low Environment Satisfaction 
"""