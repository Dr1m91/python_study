enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'evil_enemy',
    'image': ['image1.jpg','image2.jpg','image3.jpg']
}
all_enemies = []
#all_enemies.append(enemy)
#all_enemies.append(enemy)
#all_enemies.append(enemy)

#print(all_enemies)

for x in range(0,10):
    all_enemies.append(enemy.copy())
    print(x)

all_enemies[4]['health'] = 30
all_enemies[9]['name'] = 'kozel'
all_enemies[1]['loc_x'] = all_enemies[1]['loc_x'] + 30
all_enemies[2]['loc_x'] += 30
for i in all_enemies:
    print(i)
print(all_enemies[1])
