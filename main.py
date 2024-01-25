A = set()
B = set()

while True:
    x = input("Please input set A (type end to end): ")
    if not x.lower() == "end":
        A.add(x)
    else:
        print("Thank you.")
        break

while True:
    x = input("Please input set B (type end to end): ")
    if not x.lower() == "end":
        B.add(x)
    else:
        print("Thank you.")
        break

print("Intersection of A and B is: ", A.intersection(B))