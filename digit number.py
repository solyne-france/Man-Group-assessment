pp = open('numbers.txt')
content = pp.read()
print(content)
data = content.split()
print(data)
count = 0 

for i in data:
    for letter in i:
        if(i.isdigit()):
            count=count+1
print(" numbers of digits in  numbers.txt file",count)


