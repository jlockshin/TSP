
n = 5
x = 0

"""
for i in range(1, n+1):  # we want to include n
    for j in range(i, ((2*n) + 1)):
        x += 1
        print("This is i: " + str(i) + " This is j: " + str(j))
print(str(x))
"""

for i in range(1, n+1):
    for j in range(i, ((2*i) + 1)):
        x += 1
        print("This is i: " + str(i) + " This is j: " + str(j))
print(str(x))