text = input("Enter text : ")
count =0
for i ,char in enumerate(text):
    if char == 'a':
        count+=1
print(count)