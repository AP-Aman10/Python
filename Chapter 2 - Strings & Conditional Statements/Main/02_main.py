String = "Har Har Mahadev"

length = len(String)

print(f"Original String          := {String}")
print(f"Length of String         := {length}\n")

# Basic slices
print(f"Full String [::]         := {String[::]}")
print(f"Last 15 chars [-15:]     := {String[-15:]}")
print(f"First 12 chars [:12]     := {String[:12]}")
print(f"From index 4 [4:]        := {String[4:]}\n")

# Extra slices
print(f"First word [:3]          := {String[:3]}")
print(f"Second word [4:7]        := {String[4:7]}")
print(f"Last word [-7:]          := {String[-7:]}")
print(f"Every 2nd char [::2]     := {String[::2]}")
print(f"Reverse string [::-1]    := {String[::-1]}")
print(f"Reverse every 2nd [::-2] := {String[::-2]}\n")

# Slicing with ranges
print(f"Middle part [2:12]       := {String[2:12]}")
print(f"'Mahadev' part [8:15]    := {String[8:15]}")
print(f"Skip first & last [1:-1] := {String[1:-1]}")
