lst = []

n = int(input("NO OF ELEMENTS:     "))

for i in range(n):
              element = int(input("ELEMENTS: "))
              lst.append(element)
            
print("\nINPUT LIST 1 = ", lst)

for a in lst:
    if a<0:
        lst.remove(a)
print("\nLIST 2 = ", lst)
              
