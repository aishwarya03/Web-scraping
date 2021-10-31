#Patient_first_name= "John"
#Patient_last_name= "Smith"
#Patient_age=20
#print(Patient_last_name,Patient_first_name,Patient_age)
#greeting= input("what is your name? ")
#("hello " +greeting)

#abnd_width= input("tell your version: ")
#company_width= input("tell your company version: ")
#answer_to_you_is= int(abnd_width)+float(company_width)
#print("the current version is "+ str(answer_to_you_is))

#weight_n=float(input("Enter weight: "))
#convert_n=str(input("K(g) or L(p): "))
#if convert_n== 'K' or 'k':
   # your_weight= weight_n*1000
#else: your_weight= weight_n*100
#print("enter weight "+str(your_weight) )


#o = [7, 2, 8, 4, 10]
#min=o[0]
#for i in range(len(o)-1):
    #f min > o[i]:
        #min=o[i]
#print(min)

#o = [7, 2, 8, 4, 10]
#print(range(5))


#min="hello.!,,,,,,,?!"
#pun = ".?!, "

#for item in min:
    #flag=True
    #for punctuation in pun:
        #if item == punctuation:
            #flag=False
            #break
    #if flag==True:
        #print(item)

#dict={
   # "brand":"maruti",
    #"carname" : "suzuki",
    #"1brand":"lko",
#}
#print(dict["brand"])

#l=[9,9,0,"a"]
#t= {1,2,4,4,8}
#print(l)


'''n=int(input("give number: "))
rev=0
while n!=0:
    rev=rev*10+n%10
    n=n//10
print(rev)
'''
'''
n=0
p=554
c=str(p)
for item in c:
    n=n+int(item)**3
if n==p:
    print("y")
else: print("n")


n=[4,6.9,0]
n.reverse()
print(n)
#print(c[::-1])
'''
# PRIME OR NOT
'''
n=int(input("give number: "))
flag = True
if n>1:
    for item in range(2,n):
        if n%item==0:
            flag = False
if flag==True:
    print("prime")
else:
    print("not prime")
'''
#0 1 1 2 3 5 8..
#FIONACCI SERIES
'''
import numpy as np
n=10
fibseries = np.zeros((n+2,1), dtype = int)
a=0
b=1
fibseries[0]=a
fibseries[1]=b
print(a)
print(b)
for i in range(n):
    c=a+b
    a=b
    b=c
    p=i+2
    fibseries[p]=c
    print(c)
print(fibseries)
summ=np.sum(fibseries)
print(summ)

s="not"
c=s[::-1]
if s==c:
    print("palindrom")
else:
    print("not palindrom")
'''
#greatest of three number
'''
import numpy as np
n=[1, 3, 6]
max=np.amax(n)
print(max)
max=np.argmax(n)
print(max)
'''
# binary or not
'''
n=898
p=str(n)
for item in p:
    flag=True
    if int(item)>1:
        flag=False
        break
if flag:
    print(" birany")
else: print("it not binary")

def addd(num1):
    num2=0
    for item in num1:
        num2+=int(item)
    print(f"sum {num2}")
addd("999")
'''
# CHECK BINARY USING RECURSION METHOD
'''
def is_binary_or_not(strr):
    if strr==0:
        print("binary")
        return 0
    if strr%10>1:
        print("not binary")
        return 0
    else:
        return(is_binary_or_not(strr//10))
is_binary_or_not(1001)
'''
# SWAP TWO NUMBERS WITHOUT THIRD VARIABLE
'''
a=3
b=5
a=a+b
b=a-b
a=a-b
print(a,b)
'''
# PRIME FACTORS OF AN INTEGER
'''
n=5
l=[]
while n%2==0:
    l.append("2")
    n=n//2
for item in range(3,n+1,2):
        print(item)
        for item1 in range(2, item):
            print(item1,"a")
            is_prime=True
            if item % item1 == 0:
                is_prime = False
                break
        print(is_prime,"aa")
        if is_prime:
            while n % item == 0:
                l.append(item)
                n = n // item
print(l)
'''
# sum of integer without arthematic operator
'''
a=5
b=3
l=[]
for item in range(a):
    l.append(item)
for item1 in range(b):
    l.append(item1)
print(len(l))
'''
# learn enumeration
'''
data = ['a', 'b', 'c']
for (indx,item) in enumerate(data):
    print(item, indx)
print("===")
for indx in range(len(data)):
    print(data[indx], indx)