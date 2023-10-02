import re
pattern = 'phone'
index = re.search(pattern,"My phone number")
print(index)
print(index.span())

matches = re.findall(pattern,"mY phone phone phone ne")
print(matches)

phone_number = "837-298-1838"
rs=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',phone_number)
rs2=re.search(r'\d{3}-\d{3}-\d{4}',phone_number)

print(rs)
print(rs.group())
print(rs2)
print(rs2.group())

# ....