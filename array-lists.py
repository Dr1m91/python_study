cities = ['New York','Moscow', 'new dehli', 'Simferopol', 'Toronto']

print(cities)
print(len(cities))
print(cities[3])
print(cities[-1])
print(cities[2].title())
cities[2] = 'Tula'
print(cities)


cities.append('Orenburg')
cities.append('Kurgan')
print(cities[5])

cities.insert(2, 'Vorkuta')
print(cities)



del cities[1]
