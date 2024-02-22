---
title: "Modifying Data Frames in R"
output: html_notebook
---

```{r message=FALSE, warning=FALSE}
# load libraries
library(readr)
library(dplyr)
```

```{r message=FALSE}
# load data frame
dogs <- read_csv('dogs.csv')
```

```{r}
# inspect data frame
head(dogs)
```

```{r}
# add average height column
dogs <- dogs %>% # create pipe dogs
  mutate(avg_height = (height_low_inches + height_high_inches)/2) # new column created called avg_height with the values of the average height
head(dogs) # return the first 6 rows
```