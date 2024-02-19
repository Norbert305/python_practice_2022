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
artists # returns all of the data from the table
```

```{r}
# select all columns except one
no_albums <- artists %>% # pipe inside no_albums variable
  select(-albums) # column excluded with the (-) minus symbol
no_albums # data from variable returned
```

```{r}
# select all columns except a set
# pipe stored is variable df_cols_removed
df_cols_removed <- artists %>% # same logic applies here with multiple columns deselected
  select(-genre,-spotify_monthly_listeners,-year_founded)
df_cols_removed # return manipulated data here
```