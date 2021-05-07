act(
  go(From, To),
  %, if to is box then lighton else nothing, is this correct ((box(To),switchOn()) ; \+ box(To))
  [in(shakey, From), on_ground, connects(From,To)],
  [in(shakey, From)],
  [in(shakey, To)]
).

act(
  push(Box, From, To),
  [in(shakey, From), in(Box, From), box(Box), connects(From, To), switchOn(From), on_ground],    %Precondistions
  [in(Box, From), in(shakey, From)],    %To Delete
  [in(Box, To), in(shakey, To)]     %To Add
).

act(
  switchOnLight(Light, Room),
  [switch(Light), in(Light, Room), in(shakey, Room), switchOff(Room), ontop],    %Precondistions
  [switchOff(Room)],    %To Delete
  [switchOn(Room)]     %To Add
).

act(
  switchOffLight(Light, Room),
  [switch(Light), in(shakey, Room), in(Light, Room), switchOn(Room), ontop],    %Precondistions
  [switchOn(Room)],    %To Delete
  [switchOff(Room)]     %To Add
).

act(
  climbUp(Box, Room),
  [on_ground, box(Box), in(Box, Room), in(shakey, Room)],    %Precondistions
  [on_ground],    %To Delete
  [ontop]         %To Add
).

act(
  climbDown(),
  [ontop],    %Precondistions
  [ontop],    %To Delete
  [on_ground]     %To Add
).

goal_state(
    [
        in(shakey, room1),
        switchOff(room1),
        in(box2, room2)
    ]
).

initial_state(
    [   room(corridor),
        room(room1),
        room(room2),
        room(room3),
        room(room4),

        switch(switch1),
        switch(switch2),
        switch(switch3),
        switch(switch4),

        switchOn(room1),
        switchOff(room2),
        switchOff(room3),
        switchOn(room4),
        switchOn(corridor),

        box(box1),
        box(box2),
        box(box3),
        box(box4),

        connects(corridor, room1),
        connects(corridor, room2),
        connects(corridor, room3),
        connects(corridor, room4),

        % For two-way definitions
        connects(room1, corridor),
        connects(room2, corridor),
        connects(room3, corridor),
        connects(room4, corridor),
        % -----------------------

        in(switch1, room1),
        in(switch2, room2),
        in(switch3, room3),
        in(switch4, room4),

        in(box1, room1),
        in(box2, room1),
        in(box3, room1),
        in(box4, room1),

        shakey,
        on_ground,
        in(shakey, room3)
    ]
).

