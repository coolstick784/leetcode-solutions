# Write your MySQL query statement below
with tmp1 as (
    select t.*, u.banned as cli_banned, u2.banned as dri_banned from Trips t
    join Users u
    on t.client_id = u.users_id
    and u.banned = 'No'
    join Users u2
    on t.driver_id = u2.users_id
    and u2.banned = 'No'
    where u.banned = 'No' and u2.banned = 'No'
),
tmp2 as ( 
select date(request_at) as Day, count(*) as ct_cancelled
from tmp1
 where status like "cancelled%" 
 group by date(request_at)

),
tmp3 as (
    select date(request_at) as Day, count(*) as ct_total
    from tmp1
    group by date(request_at)
)

select distinct date(aa.request_at) as Day, coalesce(round(a.ct_cancelled/b.ct_total, 2), 0.00) as "Cancellation Rate"
from Trips aa
left join tmp2 a
on date(aa.request_at) = a.Day
left join tmp3 b
on date(aa.request_at) = b.Day
where b.ct_total is not null 
and date(aa.request_at) between '2013-10-01' and '2013-10-03'
