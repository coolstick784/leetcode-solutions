-- Write your PostgreSQL query statement below
with max_date_df as (select product_id, new_price, change_date, max(change_date) over (partition by product_id) as max_date
from Products
where change_date <= '2019-08-16'),

not_missing as (select product_id, new_price as price
from max_date_df
where change_date = max_date)
select distinct pro.product_id, coalesce(nm.price, 10) as price
from Products pro
left join not_missing nm
on pro.product_id = nm.product_id; 

