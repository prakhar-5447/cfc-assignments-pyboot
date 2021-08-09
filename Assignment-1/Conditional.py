"""
Take credits
If credits is greater than or equal to 7500 then
Display "Tera Leader"
Else
If credits is greater than or equal to 6000 and lesser than 7000 then
Display "Gega Leader"
Else
If credits is greater than or equal to 4500 and lesser than 6000 then
Display "Mega Leader"
Else
otherwise
Display "Rising Star"
"""

credits = int(input("ENTER YOUR CREDITS : "))
if credits>=7500 :
    print("Tera Leader") 
elif 6000<=credits & credits<7000 :
    print("Gega Leader")
elif 4500<=credits  & credits<6000 :
    print("Mega Leader")
else :
    print("Rising Star")
