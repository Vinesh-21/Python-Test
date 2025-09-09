def rotateLeft(d, elements: list):
   
   lenght = len(elements)
   d = d % lenght
   1
   return elements[d:] + elements[:d]

d = int(input("Number Of Rotation -> " ))

elements = input("Enter the List -> ")

elements = list(map(int, elements.split()))

print(rotateLeft(d, elements))