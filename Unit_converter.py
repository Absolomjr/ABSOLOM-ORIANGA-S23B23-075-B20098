print()
print("***UNIT CONVERTER")
print()

conversions_available =[(0, 'km','mi'),
                        (1, 'mi','km'),
                        (2, 'kg','Ibs'),
                        (3, 'Ibs','kg'),
                        (4, '*F','*C'),
                        (5, '*C','*F')

]
print("conversions available:")
print()
for conversion_number, from_unit, to_unit in conversions_available:
    print(f"{conversion_number} {from_unit} -> {to_unit}")

print()
conversion =input("Enter the number of conversion to use -->")  
conversion_index =int(conversion) 

conversion_number, from_unit, to_unit= conversions_available[conversion_index]
print()
from_value =float(input(f"Enter {from_unit} -->"))
print()

if conversion_number ==0:
    to_value =from_value *0.62
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")

elif conversion_number ==1:
    to_value =from_value *1.61
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")

elif conversion_number ==2:
    to_value =from_value *0.45
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")

elif conversion_number ==3:
    to_value =from_value *2.22
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")

elif conversion_number ==4:
    to_value =(from_value -32) /1.8
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")

elif conversion_number ==5:
    to_value =from_value *1.8 +32
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")
