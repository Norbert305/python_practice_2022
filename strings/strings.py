

intro = "My name is Jeff!"


print(intro.lower()) # prints 'my name is jeff!'
print(intro.upper()) # prints 'MY NAME IS JEFF!'
print(intro.title()) # prints 'My Name Is Jeff!'


intro = "My name is Jeff!"
print(intro.split()) # prints ['My', 'name', 'is', 'Jeff!']
print(intro.split('name')) # prints ['My ', ' is Jeff!']
print(intro.split('!')) # prints ['My name is Jeff', '']