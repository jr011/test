a = [1,2,3,4,5,6]
b = a[6]
print(b)
def adder(n):
     num = 0
     while num < n:
         yield num
         num += 1
     return num  #Noncompliant

adder(b)