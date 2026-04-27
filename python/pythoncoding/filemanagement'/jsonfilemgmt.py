import json
import os

def write_json(filename):
    data = [
        {'name':'chetan','age':23},
        {'name':'utkarsh','age':23}
    ]
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Wrote successfully")

def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        for person in data:
            print(f"Name: {person['name']}, Age: {person['age']}")

def delete_json(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print('File got deleted')
    else:
        print("File does not exist")

filename = "myfile.json"
write_json(filename)
print("Data read from JSON file:")
read_json(filename)
delete_json(filename)