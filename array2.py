#          0     1      2         3         4
import string

cars = ['bmw', 'vw', 'opel', 'shkoda', 'Lada']
for i in cars:
    print(i.title())
    print(i.upper())
for i in range(20,26):
    print(i)
mynumber_list = list(range(0, 10))
print(mynumber_list)
print("=============================")
for x in mynumber_list:
    x = x*2
    print(x)
mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is:  " + str(max(mynumber_list)))
print("Max number is:  " + str(min(mynumber_list)))
print("Max number is:  " + str(sum(mynumber_list)))

print("=============================")
print("=============================")
print("=============================")


#          0     1      2         3         4
import string

cars = ['bmw', 'vw', 'opel', 'shkoda', 'Lada']
mycars = cars[0:3]
print(mycars)
mycars = cars[:3]
print(mycars)
mycars = cars[-3:]
print(mycars)
mycars = cars[-3:-1]
print(mycars)
mycars = cars[:]

