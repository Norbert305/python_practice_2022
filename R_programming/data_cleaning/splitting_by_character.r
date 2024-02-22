


# Create the 'user_type' and 'country' columns
df %>%
  separate(type,c('user_type','country'),'_')

# From:
id	    type
1011	“user_Kenya”
1112	“admin_US”
1113	“moderator_UK”

#To:
id	    user_type	    country
1011	“user”	        “Kenya”
1112	“admin”	        “US”
1113	“moderator”	    “UK”


# Notes:

# type is the column to split

# c('user_type','country') is a vector with the names of the two new columns

# '_' is the character to split on