-- Write your PostgreSQL query statement below
with rank_joined as 
( 
    select dept.name as Department, emp.name as Employee, emp.salary as Salary, dense_rank() over (partition by departmentId order by salary desc) as sal_ranking
    from
    Employee emp
    inner join Department dept
    on emp.departmentId = dept.id
)
select Department, Employee, Salary
from rank_joined
where sal_ranking <= 3;
