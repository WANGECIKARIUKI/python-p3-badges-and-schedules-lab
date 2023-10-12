def badge_maker(name):
    name = "Hello, my name is Guido van Rossum."
    return name

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = []
    for index, name in enumerate(names, start= 1):
        rooms.append(f"Hello, {name}! You'll be assigned to room {index}!")
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print (badge)

    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
