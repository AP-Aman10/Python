elements = [10, "Aman", False, "This", "Preet", "Shubham", "Prince"]

i = 0
while i < len(elements):
    if type(elements[i]) is int:
        print(f"{elements[i]}:= Int")
    elif type(elements[i]) is float:
        print(f"{elements[i]}:= Float")
    elif type(elements[i]) is str:
        print(f"{elements[i]}:= String")
    elif type(elements[i]) is bool:
        print(f"{elements[i]}:= Bool")
    i += 1
