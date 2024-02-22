




# Create the 'month' column
df %>%
  mutate(month = str_sub(birthday,1,2))

# Create the 'day' column
df %>%
  mutate(day = str_sub(birthday,3,4))

# Create the 'year' column
df %>%
  mutate(year = str_sub(birthday,5))



  # From:

  id	birthday
1011	“12241989”
1112	“10311966”
1113	“01052011”


# To:


id	    birthday	month	day	    year
1011	“12241989”	“12”	“24”	“1989”
1112	“10311966”	“10”	“31”	“1966”
1113	“01052011”	“01”	“05”	“2011”


