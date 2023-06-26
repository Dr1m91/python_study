city = ['New York', 'Tokyo', 'herson', 'Rostov', 'Toronto']
print(city)
print(len(city))

print(city[0+1])
print(city[0+2].title())
print(city[-1])
city[3] = 'Tula'
print(city)
city.append('Donetsk')
print(city)
city.append('Sevastopol')
city.insert(0, 'lugansk')

print(city[0].title())
del city[1]
print(city)
city.remove('Tula')
print(city)
deleted_city = city.pop()
print("Deleted city is:" + " " + deleted_city)
print(city)
city.sort()
print(city)
city.sort(reverse=True)
print(city)
city.reverse()
print(city )