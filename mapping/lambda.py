
my_list = [2,4,6,8,10]

times_three = list(map(lambda value : value * 3, my_list))

print(times_three)


# ---------------------------------------------------------------------------

even_odd_list = [1,2,3,4,5,6,7,8,9,10]

filter_out_odd = list(filter(lambda value : value % 2 == 0, even_odd_list))

print(filter_out_odd)

