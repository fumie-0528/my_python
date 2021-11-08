for i in range (150):    
    print(i)

for i in range (5,1000):
    if i % 5 ==0:
        print(i)

for i in range (1,100):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 ==0:
        print("Coding Dojo")
    else:
        print(i)

sum = 0
for i in range (1,500001, 2): 
        sum = i + sum
    print(sum)

for i in range (2018, 0, -4):
    print (i)

low_num=2
high_num=9
mult=3
for i in range(low_num, high_num + 1):
    if i % mult == 0:
        print(i)