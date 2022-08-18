pp = open('numbers.txt')
content = pp.read()
print(content)
data = content.split()
print(data)
count = 0 
for a in data:
   count=count + 1 
   
print(count)

for a in data:
    for letter in a :
        if (letter ==1):
            count=count+1
print("the numbers of digit that appears most",count)

#for i in data:
    
   # for letter in i :
    #    if (letter.isdigit()):
     #       count=count+1
#print("letter")

for i in data:
    for letter in i:
        if(i.isdigit()):
            count=count+1
print(" numbers of digits in  numbers.txt file",count)


for a in data:
    for letter in a :
        if (letter ==1):
            count=count+1
print("the missing number ",count)