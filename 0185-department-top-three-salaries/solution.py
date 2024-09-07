import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    top_3 = {}
    ids = list(department.id)
    l_id = []
    l_top_3 = []
    
    for id in ids:
        cur_df = employee[employee['departmentId'] == id]
        cur_top_3 = list(set(cur_df.salary))
        cur_top_3.sort()
        cur_top_3 = cur_top_3[-3:]
        for sal in cur_top_3:
            l_id.append(id)
            l_top_3.append(sal)
    fin_df = pd.DataFrame(list(zip(l_id, l_top_3)), columns = ['departmentId2', 'top_salary'])
    fin_df2 = fin_df.merge(employee, how='left', left_on = ['departmentId2', 'top_salary'], right_on = ['departmentId', 'salary'])[['departmentId', 'name', 'salary']]
    department.columns = ['dept_id', 'dept_name']
    fin_df3 = department.merge(fin_df2, how='inner', left_on = 'dept_id', right_on = 'departmentId')[['dept_name', 'name', 'salary']]
    fin_df3.columns = ['Department', 'Employee', 'Salary']
    return fin_df3

    

        


