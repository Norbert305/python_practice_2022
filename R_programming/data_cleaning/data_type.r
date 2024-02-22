---
title: "Data Cleaning in R"
output: html_notebook
---

```{r message=FALSE, warning=FALSE}
# load libraries
library(dplyr)
```

```{r}
# load fruit data frame
load("fruit.Rda")
```

```{r}
# print structure of students
print(str(fruit))
```

# Fruit Table

# item	    price	    calories
# “banana”	“$1”	       105
# “apple”	 “$0.75”	    95
# “peach”	 “$3”	        55



# Data Type of Fruit Table

#> $ item:        chr
#> $ price:       chr
#> $ calories:    num