
# Polymorphism in OOP is the concept of classes sharing methods with the same name.




# The code below shows two different classes that are independent of each other with some methods of the same names:

class Checking():
   def type(self):
       print('You have a checking account at the Codecademy Bank.')
 
   def balance(self):
       print('$20 left in your checking.')
 
class Savings():
   def type(self):
       print('You have a savings account at the Codecademy Bank.')
 
   def balance(self):
       print('$1000 left in your savings.')

# We can create an object for each class, and without worrying about which object belongs to which class, we can call the same methods.
account_a = Checking()
account_b = Savings()
# In the for loop, the variable account iterates through the tuple with the two objects, and executes the method for each class accordingly: 
for account in (account_a, account_b):
   account.type()
   account.balance()