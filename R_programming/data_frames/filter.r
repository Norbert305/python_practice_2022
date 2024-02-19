---
title: "Introduction to Data Frames in R"
output: html_notebook
---

```{r message=FALSE, warning=FALSE}
# load libraries
library(readr)
library(dplyr)
```

```{r message=FALSE}
# load data frame
artists <- read_csv('artists.csv')
```

```{r}
# filter rows one condition
rock_groups <- artists %>% # pipe contained in variable rock_groups
  filter(genre == 'Rock') # return all the rows with the column (called) genre with the values of 'Rock'
rock_groups # return the manipulated data
```

```{r}
# filter rows multiple conditions
popular_rock_groups <- artists %>% # pipe contained in variable popular_rock_groups
  filter(genre == 'Rock', spotify_monthly_listeners > 20000000)
popular_rock_groups # returning all of the rows the column genre having the value of 'Rock' and the column spotify_monthly_listeners with values greater than 20000000
```

# more examples here bellow:



# ```{r}
# my_order <- orders %>%
#   filter(shoe_type == 'clogs' | price < 20)
# my_orders
# ```

# ```{r}
# return_shoes_not_red <- orders %>%
#   filter(!(shoe_color == 'red'))
# return_shoes_not_red
# ```


