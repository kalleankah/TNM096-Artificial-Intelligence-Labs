room(corridor).
room(room1).
room(room2).
room(room3).
room(room4).

switch(switch1).
switch(switch2).
switch(switch3).
switch(switch4).

box(box1).
box(box2).
box(box3).
box(box4).

robot(shakey).

door(door1).
door(door2).
door(door3).
door(door4).

connects(room1, corridor).
connects(room2, corridor).
connects(room3, corridor).
connects(room4, corridor).

connects(door1, corridor).
connects(door2, corridor).
connects(door3, corridor).
connects(door4, corridor).

connects(door1, room1).
connects(door2, room2).
connects(door3, room3).
connects(door4, room4).

contains(switch1, room1).
contains(switch2, room2).
contains(switch3, room3).
contains(switch4, room4).

contains(box1, room1).
contains(box2, room1).
contains(box3, room1).
contains(box4, room1).

at(shakey, room3).
