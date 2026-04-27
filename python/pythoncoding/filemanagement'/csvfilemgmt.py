import csv
import os
def write_csv(filename):
    data=[
        {'name':'chetan','age':23},
          {'name':'utkarsh','age':23}
          ]
    columnname=['name',"age"]
    with open(filename,'w',newline="\n") as file:
        writer=csv.DictWriter(file,fieldnames=columnname)
        writer.writeheader()
        writer.writerows(data)


def read_csv(filename):
    with open(filename,"r",newline="\n") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}, Age:{row['age']}")


def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print('file got deleted')
    else:
        print("file dost not exist")

filename="myfile.csv"
write_csv(filename)
print("Data read from csv file:")
read_csv(filename)
delete_csv(filename)