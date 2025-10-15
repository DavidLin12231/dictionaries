money = {'John': 94, 'Paul': 85, 'Jason': 104}
print(money)
money['Betty'] = 92
money['Scott'], money['Joseph'] = 142, 33
x = money.pop('Joseph')

names = dict([("Alice",0),("Bob",0),("Charlie",0),("Dan",0)])


people = {x: 0 for x in ("Edward","Frank","George","Hank")}
print(people)

for keys, values in people.items():
    print(keys, values) 
