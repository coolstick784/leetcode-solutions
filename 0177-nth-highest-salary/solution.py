import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1:
        return pd.DataFrame([None], columns = [f'getNthHighestSalary({N})'])
    try:
        salary = list(set(employee.salary))
        salary.sort()
        return pd.DataFrame([salary[-1*N]], columns = [f'getNthHighestSalary({N})'])
    except:
        return pd.DataFrame([None], columns = [f'getNthHighestSalary({N})'])


    
