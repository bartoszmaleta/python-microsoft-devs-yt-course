wayne = {}
wayne['first'] = 'Wayne'
wayne['last'] = 'Rooney'
 

cristiano = {'first': 'Cristiano', 'last': 'Ronaldo'}

print()
print(wayne)
print(cristiano)

people = [wayne, cristiano]
people.append({'first': 'Leo', 'last': 'Messi'})
best_footballers = people[0:2]
print(people)
print()
print(best_footballers)
print()
print(len(best_footballers))
