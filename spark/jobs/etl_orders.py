from pyspark.sql import SparkSession 

# Create Spark session with Hive support
spark = (
    SparkSession.builder
    .appName("ReadFromHDFS") 
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") 
    .enableHiveSupport() 
    .getOrCreate()
)

from pyspark.sql.functions import col, sum, month
from pyspark.sql import functions as F

# Read orders data from HDFS
order_df = spark.read.parquet("hdfs://localhost:9000/user/student/orders")

order_df.show(5)

# Add total_amount column (price * quantity)
order_df = order_df.withColumn("total_amount", col("price") * col("quantity"))

# 1. Total Sales per Customer – Calculate total amount each customer spent.
total_sales_per_customer = (
    order_df.groupBy("customer_name").sum("total_amount")
).show()

# 2. Total Sales per Product – Find which product generated the most revenue.
total_sales_per_product = (
    order_df.groupBy("product").sum("total_amount")
).show()

# 3. Best-Selling Product by Quantity – Find which product sold the most units.
best_selling_product_per_quantity = (
    order_df.groupBy("product")
    .sum("quantity")
    .withColumnRenamed("sum(quantity)", "total_quantity")
    .orderBy("total_quantity", ascending=False)
).show()

# 4. Daily Revenue – Calculate total revenue for each order_date.
total_revenue = (
    order_df.groupBy("order_date").sum("total_amount")
).show()

# 5. Customer with Highest Single Purchase – Find the order with the maximum total_amount.
highest_purchase = (
    order_df.orderBy("total_amount", ascending=False)
    .limit(1)
).show()

# 6. Average Order Value per Customer – For each customer, compute average purchase value.
avg_order_value_per_customer = (
    order_df.groupBy("customer_name").avg("total_amount")
).show()

# 7. Top 2 Customers by Total Spending – Rank customers by total amount spent.
top_customers = (
    order_df.groupBy("customer_name")        
    .agg(F.sum("total_amount").alias("total_spent"))
    .orderBy("total_spent", ascending=False)          
    .limit(2)                                        
).show()

# 8. Monthly Sales – Calculate total revenue grouped by month.
orders_df = order_df.withColumn(
    "order_date",
    (F.col("order_date") / 1000).cast("timestamp")   # تحويل Unix timestamp لتاريخ
)

monthly_sales = (
    orders_df.groupBy(F.month("order_date").alias("month"))
    .agg(F.sum(F.col("quantity") * F.col("price")).alias("monthly_sales"))
    .orderBy("month")
)

monthly_sales.show()

# 9. Product Popularity – Count how many times each product was purchased.
product_popularity = order_df.groupBy("product").count().show()

# Save the final DataFrame into Hive as orders_hive
order_df.write.mode("overwrite").saveAsTable("orders_hive")
