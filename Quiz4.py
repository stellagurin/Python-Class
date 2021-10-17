# Question 1 - 10 loops
total_upper = 0

word1 = "UniverSiTY of GoErGia"
word2 = "CSCi 1300"

for letter in word1:
  if letter.isupper():
    total_upper += 1
   
for letter in word2:
  if letter.isupper():
    total_upper += 1
    
print(total_upper)

# Question 2 - count = 50
count = 0

for i in range(100):
  if i == 5:
    break
  for j in range(100):
    if j == 10:
      break
    count += 1
    
print(count)

# Question 3 - loop from 0 - 99
for i in range(10):
  for j in range(10):
    print(i*10+j)

for i in range(100):
  print(i)

# Question 4 - Clifford printed 6 times
shows = ["Clifford", "Blues Clues", "Dora the Explorer"]

for i in shows:
  for j in shows:
    if i == "Clifford":
      print(i)
    if j == "Clifford":
      print(j)
      
# Question 5 - Hello printed 0 times
for i in range(0,100,2):
  if i % 2 == 1:
    print("Hello")
    
# Question 6 - A function is a series of statements that can be called.

# Question 7 - valid way to define a function : def foo(): and def foofoo():

# Question 8 - true statements : global variables can be used anywhere local variables can be used
# AND local variables cannot be used outside of the scope of the function they were defined in.
# AND global variables are declared in the outermost scope

# Question 9 - output a = 54, b = 18
a = 2
b = 2

def triple(number):
  return number * 3

a = triple(a)
b = triple(a)
a = triple(b)

print(a)
print(b)

# Question 10 - A variable in a def statement that specifies an argument is refered to as a parameter

