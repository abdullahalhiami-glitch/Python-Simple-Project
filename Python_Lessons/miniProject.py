"""
هذا التطبيق عبارة عن نظام كاشير مصغر 
يحاكي عملية الدفع وطبع الفواتير 
"""

#1- Welcome Message
print('*********Welcome*********')

#2-Declare Variables
username='malek'
password='123'
bill=""
total=0.0
counter=1

#3-Start The Programm
while True:
    currentusername=input('Enter User Name?')
    currentpass=input('Enter Password')
    if currentusername==username and password==currentpass:
        product=input("Enter The Product or 'done' if you done ?").lower().strip()
        if product == "":
            print('product can not be None')
            break
        if product=="done":
            break
        else:
            price=input('Enter The Product price?')
            if price =="" or not price.isdigit():
                print('price can not be None or String')
                break
            price=float(price)
            bill+=f"{counter}-{product.capitalize()}\t{price}\n"
            counter+=1
            total+=price
    else:
        print('The Password or Username are False Try Again')

#4-Make Discount
if total>=3000:
    dicount_value=total*0.15
    total_after=total-dicount_value
else:
    dicount_value=0
    total_after=total


#5-Print The Bill
print('*********Bill*********')
print(bill)
print("*********************")
print(f'Total {total} YR')
print(f'Total After Discount {total_after} YR')
print(f'Your Discount is {dicount_value} YR')
print('*********Thank You*********')

