
my_list = ["Bob", "Bert", "Ashly", "Tasha"]

def contact_list(value):

    return f"Today I went shopping with {value} at the mall"

new_list = list(map(contact_list, my_list))

print(new_list)
