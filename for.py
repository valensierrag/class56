# I want to print a multiplication table from 1 to 10
for i in range(1,11):
    for j in range(i, 11):
        print(i, "x", j, "=", i*j)
    print()