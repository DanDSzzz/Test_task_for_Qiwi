# order
# +----------------+
# | order_id       |
# | date_time      |
# | amount         |
# | customer_id    |
# +----------------+
#
# customer
# +----------------+
# | customer_id    |
# | fio            |
# | age            |
# +----------------+
#
# Для каждого посетителя найти максимальный интервал между заказами в днях.

# CREATE TABLE customers (
#     customer_id INT PRIMARY KEY,
#     fio VARCHAR(255),
#     age INT
# );
#
# CREATE TABLE orders (
#     order_id INT PRIMARY KEY,
#     date_time DATE,
#     amount DECIMAL(10, 2),
#     customer_id INT,
#     FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
# );
#
# INSERT INTO customers (customer_id, fio, age) VALUES (1, 'Иванов Иван Иванович', 30);
# INSERT INTO customers (customer_id, fio, age) VALUES (2, 'Петров Петр Петрович', 25);
#
# INSERT INTO orders (order_id, date_time, amount, customer_id) VALUES (1, '2023-04-01', 100.00, 1);
# INSERT INTO orders (order_id, date_time, amount, customer_id) VALUES (2, '2023-04-03', 200.00, 2);
# INSERT INTO orders (order_id, date_time, amount, customer_id) VALUES (3, '2023-04-04', 150.00, 1);
# INSERT INTO orders (order_id, date_time, amount, customer_id) VALUES (4, '2023-04-06', 250.00, 2);
# INSERT INTO orders (order_id, date_time, amount, customer_id) VALUES (5, '2023-04-07', 300.00, 1);
#
# WITH OrderedOrders AS (
#   SELECT
#     customer_id,
#     order_id,
#     date_time,
#     LAG(date_time) OVER (PARTITION BY customer_id ORDER BY date_time) AS prev_date_time
#   FROM
#     orders -- Исправлено имя таблицы, так как 'order' является зарезервированным словом
# ),
# Diffs AS (
#   SELECT
#     customer_id,
#     order_id,
#     DATEDIFF(date_time, prev_date_time) AS day_diff -- Изменен порядок аргументов и удалено 'day', так как в MySQL DATEDIFF возвращает разницу в днях по умолчанию
#   FROM
#     OrderedOrders
#   WHERE
#     prev_date_time IS NOT NULL -- Исключение первого заказа каждого клиента
# )
#
# SELECT
#   customer_id,
#   MAX(day_diff) AS max_interval
# FROM
#   Diffs
# GROUP BY
#   customer_id;


# Дана таблица sales с полями product_id (идентификатор продукта), order_id (идентификатор заказа) и amount (сумма продажи).
# Необходимо для каждого продукта ранжировать заказы по убыванию суммы продажи.



# CREATE TABLE sales (
# product_id INT PRIMARY KEY,
# order_id INT,
# amount DECIMAL(10, 2)
# );
#
# INSERT INTO sales  (product_id, order_id,  amount) VALUES (1, 4, 100.00);
# INSERT INTO sales  (product_id, order_id,  amount) VALUES (2, 1, 200.00);
# INSERT INTO sales  (product_id, order_id,  amount) VALUES (3, 5, 150.00);
# INSERT INTO sales  (product_id, order_id,  amount) VALUES (4, 3, 250.00);
# INSERT INTO sales  (product_id, order_id,  amount) VALUES (5, 2, 300.00);
#
#
# SELECT s1.product_id, s1.order_id, s1.amount
# FROM sales s1
# INNER JOIN (SELECT product_id, SUM(amount) AS total_sales
# FROM sales
# GROUP BY product_id) s2 ON s1.product_id = s2.product_id
# ORDER BY s2.total_sales DESC, s1.amount DESC;


