import random, readchar, os
POS_X = 0
POS_Y = 1

MAP_WIDTH = 10
MAP_HEIGHT = 10

NUM_OF_MAP_OBJECTS = 11
map_objects = []
my_position = [3,1]
while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0,MAP_WIDTH), random.randint(0,MAP_HEIGHT)]

    if new_position not in map_objects and new_position != my_position:
        map_objects.append([random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)])
repeat = True

while repeat == True:
    #os.system('clear')
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for coor_y in range(MAP_HEIGHT):
        
        print("|", end="")
        for coor_x in range(MAP_WIDTH):
            
            char_to_draw = " "
            object_in_cell = None
            
            for map_object in map_objects:
                if map_object[POS_X] == coor_x and  map_object[POS_Y] == coor_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            if my_position[POS_X] == coor_x and  my_position[POS_Y] == coor_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
            
            print(" {} ".format(char_to_draw), end="")
        print("|")
    
    print("+" + "-" * (MAP_WIDTH * 3) + "+")


#ask user pa donde moverse

#direction = input("A donde nos moveremos padrino? [WASD]: " )
    direction = readchar.readchar()
#print(direction)
    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    else:
        repeat = False
    os.system('clear')