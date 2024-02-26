# this below is use for  buying of product by costumer.

print('\n')
print('************************ WELCOME TO CHIMABEST SHOPPING MALL **************************')
N_costomer = input('Enter your Name ').upper()
L_costomer = input('Enter your location ').upper()
A_costomer = input('Enter your Age ').upper()
# products to buy in the shop for the customer
product_list = {'watch': 2000, 'shirt': 3500, 'jeans': 5000, 'perfume': 1500,
                'shoes': 7500.40, 'pole': 2500.30}

# show the user our products list
print('This is the list of our product')
for i in product_list:
    print(i)

n_pro = int(input('Enter the number of our products you want to buy '))

# n_list = {'watch': 2000, 'shirt': 3500, 'jeans': 5000, 'perfume': 1500, 'shoes': 7500, 'pole': 1500}

p1_list = []
p2_list = []
if n_pro <= 6:
    for x in range(n_pro):
        p1 = input('Enter the name of product you want to buy ' + str(x + 1) + ' ').lower()
        p1_list.append(p1)

        p2 = int(input('Enter the quantity of product you want ' + str(x + 1) + ' '))
        p2_list.append(p2)

        for x in product_list.keys():
            if p1 in x:
                xn = product_list.get(x)
                print('price per product =', xn)
                xt = (xn * p2)
                print('total price =', xt)

else:
    print('Invalid Entry')
get_value = []

print('List of product bought    =', p1_list),
print('quantity of products bought =', p2_list, 'respectively'),
print('\n'),

print('*********************** CHIMABEST SHOPPING MALL * **********************************'),
print('******************************* RECEIPT ********************************************'),
print('Name       :' + N_costomer),
print('Location   :' + L_costomer),
print('Age        :' + A_costomer),
print('Products   =', p1_list),
print('Quantity   =', p2_list),
print('Total Cost =', ),
print('************************* THANK YOU FOR SHOPPING WITH US **************************')

f = open("assignment.txt", "a")
f.write()

