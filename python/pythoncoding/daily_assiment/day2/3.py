color={'Red','Black','Brown','White','Green'}
print('Orginal set: ',color)

color.add('Blue')
color.remove('Red')
print('Updated Set',color)

color2={'Red','Pink','Gray','Black'}
print('Union :',color.union(color2))
print('Inertion :',color.intersection(color2))
print('Difference :',color.difference(color2))

check_color='yellow'
print(f"Is {check_color} in set?{check_color in color}")

fruits=['apple','banana','apple','Kiwi']
uniq_fruits=set(fruits)
print(f"unique fruits{uniq_fruits}")
