# Big Data Task — MariaDB → Sqoop → Spark → Hive

## Overview
This repository demonstrates a very simple ETL pipeline:
**MariaDB (orders)** → **Sqoop import (Parquet on HDFS)** → **Spark (transformations & analytics)** → **Hive (store results)**.


## Prerequisites
- Hadoop (HDFS + YARN) running
- Sqoop installed and in PATH
- Spark (compatible with your Hadoop version)
- Hive + Hive Metastore
- Hue (optional for UI)
- MariaDB with `orders` table (or use `sql/create_orders.sql` to create)
- JDBC driver: add `mysql-connector-java.jar` or `mariadb-java-client.jar` to `$SQOOP_HOME/lib` and `$SPARK_HOME/jars/` if needed

## Step-by-step instructions

### 1. Prepare source DB (MariaDB)
Run the SQL in `sql/create_orders.sql` to create the `orders` table and insert sample rows.

### 2. Start Hadoop & Hue
```bash
# start HDFS & YARN (on your cluster)
start-dfs.sh
start-yarn.sh

# optional: start Hue
sudo systemctl start hue
```

Check NameNode UI: http://<namenode-host>:9870
Check YARN UI: http://<resourcemanager-host>:8088
Hue UI: http://<host>:8888
