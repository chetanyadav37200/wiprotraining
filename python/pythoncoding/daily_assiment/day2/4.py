



details={'Name':'Chetan','Age':'23','Hobby':'Chess'}
print(f"Dictionary : {details}")

print(f"Name :{details['Name']}")

details['fav_food']='Poha'
details['Hobby']='Gym'
print(f"Updated dictionary :{details}")

print(f"Keys of dictionary :{details.keys()}")
print(f"Values of dictionary :{details.values()}")

del details['Age']
print(f"New Details :{details}")