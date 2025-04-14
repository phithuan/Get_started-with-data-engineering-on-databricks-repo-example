# Databricks notebook source
# MAGIC %md
# MAGIC ## Cluster trong Databricks
# MAGIC ![](/Volumes/workspace/ny_taxi/data_xe/Screenshot 2025-04-14 211535.png)
# MAGIC
# MAGIC | **ALL PURPOSE CLUSTER**                                                                 | **JOB CLUSTER**                                                                 |
# MAGIC |-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
# MAGIC | - Tạo bằng tay                                                                          | - Tạo tự động                                                                   |
# MAGIC | - Có thể sử dụng bất kỳ lúc nào                                                         | - Chỉ dùng khi job được start và sẽ được tắt khi job kết thúc                   |
# MAGIC | → không sử dụng nữa thì tắt hoặc hẹn chế độ tự động tắt khi không dùng nữa              |                                                                                 |
# MAGIC | - Thích hợp sử dụng cho hoạt động dev                                                   | - Thích hợp sử dụng cho hoạt động auto trong môi trường production              |
# MAGIC |                                                                                         | - Chỉ dùng riêng cho một job cụ thể                                             |
# MAGIC |                                                                                         | - Có thể chia sẻ giữa nhiều người dùng                                          |
# MAGIC

# COMMAND ----------


