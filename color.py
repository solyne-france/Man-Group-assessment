#before you open the file you need to save it on the folder name e.g man group assessment
pp = open('colours.txt')
# we use pp.read instead of'r'
content = pp.read()
print(content)
file= content.split()
print(file)
count = 0 

for i in file:
    count=count+1
    
print(count)

for i in file:
 
    if i=='blue':
        count=count+1
    
print(count)

for i in file:
     
    if i=='Green':
        count=count+1
    
print(count)

for i in file:
     
    if i=='Red':
        count=count+1
    
print(count)

for i in file:
     
    if i=='blue':
        count=count+1
    
print("the colour that appeared the most")