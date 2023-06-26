

def create_record(name, telephone, address):
    """Create record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

user1 = create_record('Vasya','+713201132434','Tajikiston')
user2 = create_record('Kolya','+7931232434','Uzbeikiston')
user3 = create_record('Petya','+767501132434','Turkmeniston')

print(user1)
print(user2)


def give_award(medal,*persons):
    """Give medals to persons"""
    for person in persons:
        print('Tajik ' + person.title() + ' nagrajdayetsya medalyu ' + medal)
give_award('Za Donbass', "petya", 'kolya', 'gogi')
give_award('Za Bakhmut', "Vasya", 'Sanya', 'gogen')
