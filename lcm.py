largest = int(input("Enter a number: "))
smallest = int(input("Enter a number: "))
l1 = largest
s1 = smallest
while(smallest):
    store = smallest
    smallest = largest % smallest
    largest = store
#a * b = lcm * hcf
lcm = (s1 * l1) / largest
print("The LCM is: ", lcm)