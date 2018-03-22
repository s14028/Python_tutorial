print("Hello world")

map = {5 : 'A'}

map.get(7, 'B')

array = set(1, 2, 3)
array1 = set(2, 3, 4)

array | array1 % lub
array & array1 % i
array - array1 % A\B
array ^ array1 % XOR


name = "Unix"
print(name)

array = ['String', 1]
array.insert(5, 2)
print(array[0:3])

map = {5 : 'A',
       6 : 'B',
       7 : 'Z'}
print(map[5])

if map[5] == 'A' and map[6] == 'B' :
  print('A')
else :
  print('B')
if map[6] == 'Z' :
  print('Z')
elif map[7] == 'ZZ' :
  print('B')
else :
  print('Z')
  print('B')

for x in range(0, 10) :
  print(x)
class W:
  __name = None

  def __init__(this, name):
    this.__name = name

  def show(this):
    print(this.__name)
dog = W('Name')
dog.show()
