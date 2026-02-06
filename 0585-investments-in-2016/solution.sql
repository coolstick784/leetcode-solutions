# Write your MySQL query statement below
with tmp1 as (
    select *, count(*)  over(partition by tiv_2015) as ct_tiv, count(*) over (partition by lat, lon) as ct_loc from Insurance 
)
select distinct round(sum(tiv_2016) over (),2) as tiv_2016 from tmp1
where ct_tiv > 1 and ct_loc = 1




