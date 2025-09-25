#!/bin/bash

# Import data from MariaDB orders table into HDFS as Parquet
sqoop import \
  --connect jdbc:mysql://localhost:3306/Task \
  --username YOUR_USERNAME \
  --password YOUR_PASSWORD \
  --table orders \
  --target-dir /user/student/orders \
  --as-parquetfile \
  --num-mappers 1
