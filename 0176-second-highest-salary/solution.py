import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values(by='salary')
    try:
        salary = list(set(employee.salary))
        salary.sort()
        salary = [salary[-2]]
    except:
        salary = [None]
    return  pd.DataFrame(salary, columns = ['SecondHighestSalary'])
