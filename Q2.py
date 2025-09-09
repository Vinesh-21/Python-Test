def rotateLeft(d, elements: list):
   
   lenght = len(elements)
   d = d % lenght
   
   return elements[d:] + elements[:d]

d = int(input("Number Of Rotation -> " ))

elements = input("Enter the List -> ")

elements = list(map(int, elements.split()))

print(rotateLeft(d, elements))