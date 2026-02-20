-- Write your PostgreSQL query statement below
with all_joined as  (
    select sales.sales_id, sales.name, c.name as company_name
    from SalesPerson sales
    left join Orders o
    on sales.sales_id = o.sales_id
    left join Company c
    on o.com_id = c.com_id
    where c.name = 'RED'

)
select sales.name 
from SalesPerson sales
left join all_joined a
on sales.sales_id = a.sales_id
where sales.name not in (select distinct name from all_joined);

