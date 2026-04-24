cities = ('Mumbai','Manali','Goa')
print("Orginal :",cities)
print("First City :",cities[0])
print('Last City',cities[len(cities)-1])
cities_more=('Greater Noida','Udaipur')
all_cities=cities+cities_more
print('Concatenated :',all_cities)

try:
    cities[0]='pune'
except TypeError as e:
    print("Error :",e)
a,b,c=cities
print('unpacked value:')
print(a)
print(b)
print(c)
