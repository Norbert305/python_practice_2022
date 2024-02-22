---
title: "Data Cleaning in R"
output: html_notebook
---

# head() — display the first 6 rows of the table
# summary() — display the summary statistics of the table
# colnames() — display the column names of the table


```{r message=FALSE, warning=FALSE}
# load libraries
library(readr)
library(dplyr)
```

```{r message=FALSE}
# read CSVs
grocery_1 <- read_csv('grocery_1.csv')
grocery_2 <- read_csv('grocery_2.csv')
grocery_1
grocery_2
```

```{r}
# inspect data frames
head(grocery_1) # inspect the first 6 rows
head(grocery_2) # inspect the first 6 rows
summary(grocery_1) # inspect the mean (avg), min, max, length (num of rows) and median (mid)
summary(grocery_2) # inspect the mean (avg), min, max, length (num of rows) and median (mid)
print(colnames(grocery_1)) # inspect column names
print(colnames(grocery_2)) # inspect column names
```

```{r}
# clean data frame
clean_data_frame <- 2
clean_data_frame
```

