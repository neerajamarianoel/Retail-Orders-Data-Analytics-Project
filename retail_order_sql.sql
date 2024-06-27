
-- Find top 5 revenue generating products
select product_id,sum(sale_price) as revenue
from orders
group by product_id
order by revenue desc
limit 5;

-- Find the top 5 selling product in each region
with cte as(
select region,product_id,sum(sale_price) as revenue
from orders
group by region,product_id)
select * from (
select *
,row_number() over (partition by region order by revenue desc) as rn
from cte) A
where rn <=5

-- Which state has made the highest average profit?
select state,category,avg(profit* quantity) as avg_profit
from orders
group by state,category order by avg_profit desc  limit 1;

-- How many orders are made by each customer segment?
select segment, count(*) as no_of_orders
from orders
group by segment;

