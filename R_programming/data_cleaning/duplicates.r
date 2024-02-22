




# item	        price	    calories
# “banana”	    “$1”	    105 - False
# “apple”	    “$0.75”	    95 - False
# “apple”	    “$0.75”	    95 - True
# “peach”	    “$3”	    55 - False
# “peach”	    “$4”	    55 - False
# “clementine”	“$2.5”	    35 - False



```{r}
# find duplicated rows
fruits <- fruits %>%
  duplicated()
  distinct()
```


# will return:

# >> [1] FALSE FALSE TRUE FALSE FALSE FALSE




```{r}
# remove duplicated rows
fruits <- fruits %>%
  distinct()
```
#results

# item	        price	    calories
# “banana”	    “$1”	    105 - False
# “apple”	    “$0.75”	    95 - False
# “peach”	    “$3”	    55 - False
# “peach”	    “$4”	    55 - False
# “clementine”	“$2.5”	    35 - False




```{r}
# remove duplicated values
fruits <- fruits %>%
  distinct(item,.keep_all=TRUE)
```
# results

# item	        price	    calories
# “banana”	    “$1”	    105 - False
# “apple”	    “$0.75”	    95 - False
# “peach”	    “$3”	    55 - False
# “clementine”	“$2.5”	    35 - False