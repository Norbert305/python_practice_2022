---
title: "Introduction to R Syntax"
output: html_notebook
---
```{r error=TRUE}
calculate_annual_growth <- function(year_one,year_two,pop_y1, pop_y2,city) {
  annual_growth <- (((pop_y2 - pop_y1) / pop_y1) * 100) / (year_two-year_one)
  message <- paste("From", year_one, "to", year_two, "the population of", city, "grew by approximately", annual_growth, "% each year.")
  print(message)
  return(annual_growth)
}
# Write your code starting here:

city_name <- "Istanbul, Turkey"
print(city_name)
# pop_year_one <- 691000
pop_year_one <- 8831800
print(pop_year_one)
pop_year_two <- 15029231
print(pop_year_two)

pop_change <- pop_year_two - pop_year_one

print(pop_change)


percentage_gr <- (pop_change/pop_year_one) * 100

print(percentage_gr)

# annual_gr <- percentage_gr / (2017-1927)

annual_gr <- percentage_gr / (2017-2000)

print(annual_gr)

calculate_annual_growth(1927, 2017, 691000, 15029231, "Istanbul, Turkey")

```