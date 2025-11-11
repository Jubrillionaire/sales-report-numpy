import numpy as np

np.random.seed(seed=42)
sales_data_1d = np.random.randint(low=10, high=75, size=12)

print(f"Here is our 1d sales data: \n{sales_data_1d}")

print("Rows = Days, Columns = Products")


sales_table_2d = sales_data_1d.reshape(4,3)


print(f"Here is our 2d sales data: \n{sales_table_2d}")

# tshirts = 
#mugs
#cap

#4 days
#monday = 3
#tuesday = 3
#wednesday = 3
#thursday = 3


# [
# [61 24 70] 
#  [30 33 12]
#  [31 62 11]
#  [39 47 11]
#  ]
