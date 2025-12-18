data = (
    "Name => Aman Patidar "
    "DOB => 20-11-2005 "
    "Email => amanpatidar812@gmail.com "
    "Password => KnightP@96"
)
print(f"Original:= {data}\n")
print(f"{'Endswith:':12} {data.endswith('@96')}")
print(f"{'Capitalize:':12} {data.capitalize()}")
print(f"{'Replace:':12} {data.replace('KnightP@96', 'KnightR@10')}")
print(f"{'Find DOB:':12} {data.find('DOB')}")
print(f"{'Count a:':12} {data.count('a')}")