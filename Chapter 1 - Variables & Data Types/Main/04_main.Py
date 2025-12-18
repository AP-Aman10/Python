import sys

Num = 45
String = "Aman Patidar"
Float = 10.4
Bool = True

print(f"Size of int:= {sys.getsizeof(Num)} Bytes")
print(f"Size of Char:= {sys.getsizeof(String)} Bytes")
print(f"Size of Float:= {sys.getsizeof(Float)} Bytes")
print(f"Size of Boolean:= {sys.getsizeof(Bool)} Bytes")
print(f"Size of None:= {sys.getsizeof(None)} Bytes")