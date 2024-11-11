first=123
second=456
third=789
if first!=second!=third:
    print(0)
elif first==second and third:
    print(3)
elif first == second or third:
    print(2)


first=42
second=69
third=42
if first == second or third:
    print(2)
elif first==second==third:
    print(3)
elif first!=second!=third:
    print(0)