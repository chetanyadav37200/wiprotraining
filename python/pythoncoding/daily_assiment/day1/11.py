def check_vowel(c):
    vowel=['a','e','i','o','u']
    for val in vowel:
        if(c==val):
            return True
    return False
#main
s1=input("Enter String")
count=0
for c in s1:
    if(check_vowel(c)):
        count+=1
print(count)