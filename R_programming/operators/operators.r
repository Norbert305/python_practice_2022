
#----Operators-----
# > greater than
# < less than
# <= less than or equal to
# >= greater than or equal to
# == is equal to
# != is NOT equal to

# ----Logical Operators----
# &  AND operator
# | OR operator

n = 10

if (n != 11) {
    print("this is true")
}

x = 7

if (x == 7) {
    print("This is true as well" )
}

red = "red"

color = "red"

if (red == "red" & color == "red") {
    print("The color here is red")
}


message <- 'Should I pack an umbrella?'
weather <- 'cloudy'
high_chance_of_rain <- TRUE


if (weather == 'cloudy' & high_chance_of_rain) {
  message <- "Pack umbrella!"
} else {
  message <- "No need for umbrella!"
}

print(message)
