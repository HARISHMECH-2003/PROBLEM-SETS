def num_of_people(bus_stop):
    people=0
    for stop in bus_stop:
        people+=stop[0]
        people-=stop[1]
    return people

bus_stop=[(3,2),(5,3),(1,1),(6,3),(1,3)]
result=num_of_people(bus_stop)
print(result)