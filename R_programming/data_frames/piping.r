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
# inspect data frame with pipe
artists %>% # The pipe operator, or %>%, helps increase the readability of data frame code
  head() # returns the first 6 rows of data
  artists # returns the data
  

```