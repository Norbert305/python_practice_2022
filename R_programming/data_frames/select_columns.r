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
# select one column
artist_groups <- artists %>% # pipe contained in variable artist_groups
  select(group) # the column group is selected from the table
artist_groups # data from artist_groups returned with the single column group
```

```{r}
# select multiple columns
group_info <- artists %>% # second pipe contained in variable group_info
  select(group,spotify_monthly_listeners,year_founded) # multiple columns selected
group_info # data contained inside variable group_info returned with the 3 columns group,spotify_monthly_listeners,and year_founded

# print column names

  # colnames(df)

      # or
      
  # names(df)
  
```