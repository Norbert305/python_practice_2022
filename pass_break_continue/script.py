
# pass keyword

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
# Iterate through the array. if letter j is included with the list of names then exclude the names with lowercase j 
for name in names:
   if 'j' in name.lower():
       pass
   else:
       print(name) # Hannah, Manny, Ezekiel
       
       

# break keyword

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
#  If a certain condition is met, the loop stops iterating and breaks at that point. 
for name in names:
  if 'h' in name.lower():
      break
  else:
      print(name)  # Joyce
      
      
      
# continue keyword


names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
# The code above iterates through the list names to print each element name, but skips over any elements that contain the letter m.
for name in names:
  if 'm' in name.lower():
      continue
  else:
      print(name)