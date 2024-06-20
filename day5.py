'''import json
file=open("file2.json","w")
data={
"name": "Ashu",
"age": "19"
}
json.dump(data,file)'''
'''import csv
file=open("data.csv","r")
readObj=csv.reader(file)
for row in readObj:
    print(row)
file.close()'''
'''import csv
file=open("data.csv","w")
csvWriter=csv.writer(file)
header=["name","rollnumber"]
data=[
    ["name","rollnumber"],
    ["Ashu","23951A0515"]
]
csvWriter.writerow(header)
csvWriter.writerows(data)
file.close()'''
'''def square(num):
    return num*num
data=[1,2,3,4,5]
#write a program
# m to print square of the numbers
#res=[]
#for i in data:
 # res=square(i)
#res.append(res)
#map(function,iterable) 
#syntax:map(function_object,iterable)
#iterables:tuple,list,etc...
res=list(map(square,data))
print(res)
print(type(res))'''
'''def verify(age):
    if age>18:
        return True
    else:
        return False
    return age > 18
print(verify(10))
    return age > 18
ages=[12,45,23,54,13,14]
adults=list(filter(verify,ages))#filter=function
print(adults)'''
#reduce(result(of question),b(element of list)),reduce is direct value, 
#import itertools #permutation,combination  method,functools is default package
'''from functools import reduce
def sum_of_ele(a,b):
    return a+b
data=[1,2,3,4,5]
res=reduce(sum_of_ele,data)
print(res)'''
#default value=0,we can change default value by third element,output is 25
'''from functools import reduce
def sum_of_ele(a,b):
    return a+b
data=[1,2,3,4,5]
res=reduce(sum_of_ele,data,10)
print(res)'''
#lambda method

'''arr=[
    [1,2,3,4],
    [2,3,4,3],
    [3,4,5,1]
]
arr.sort(key=lambda ele:ele[2])
print(*arr,sep="\n")'''
#factorial
'''from functools import reduce
data=[1,2,3,4,5]
res=reduce(lambda a,b:a*b,data)
print(res)'''
#def verify(age):
 #   return age > 18
'''ages=[12,45,23,54,13,14]
adults=list(filter(lambda age:age>18,ages)) left=parameter
print(adults)'''                             #right=values

                                          


