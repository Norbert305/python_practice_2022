

# Follow Example Below Old table before and after gather method is used

# id  name  age  column1  column2
# 1   Bob   20    Male    Car
# 2   Mark  30    Male    Truck
# 3   Bert  25    Male    Bike

df %>% df
 gather(column1, column2, key='new_column1', value='new_column2')

# id  name  age  new_column1  new_column2
# 1   Bob   20    column1        Car
# 2   Mark  30    column1        Truck
# 3   Bert  25    column1        Bike




#---------------------------------------- Another Example

# From:

# Account	  Checking	Savings
# “12456543”	8500	  8900
# “12283942”	6410	  8020
# “12839485”	78000	  92000



df %>% df
  gather('Checking','Savings',key='Account Type',value='Amount')


# To:

# Account	    Account-Type	Amount
# “12456543”	“Checking”	  8500
# “12456543”	“Savings”	    8900
# “12283942”	“Checking”	  6410
# “12283942”	“Savings”	    8020
# “12839485”	“Checking”	  78000
# “12839485”	“Savings”	    920000
  

# Notes:

# df: the data frame you want to gather, which can be piped into gather()

# Checking and Savings: the columns of the old data frame that you want to turn into variables

# key: what to call the column of the new data frame that stores the variables

# value: what to call the column of the new data frame that stores the values






