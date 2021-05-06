goal_state(
    [
        connects(shakey, room1)
        %\+ switchOn(switch1),
        % connects(box2,room2)
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
        switchOn(switch1),
        switchOn(switch4),
        box(box1),
        box(box2),
        box(box3),
        box(box4),
        shakey,
        connects(corridor, room1),
        connects(corridor, room2),
        connects(corridor, room3),
        connects(corridor, room4),
        % connects(room1, corridor),
        % connects(room2, corridor),
        % connects(room3, corridor),
        % connects(room4, corridor),
        connects(room1, switch1),
        connects(room2, switch2),
        connects(room3, switch3),
        connects(room4, switch4),
        % connects(switch1, room1),
        % connects(switch2, room2),
        % connects(switch3, room3),
        % connects(switch4, room4),
        connects(box1, room1),
        connects(box2, room1),
        connects(box3, room1),
        connects(box4, room1),
        connects(shakey, room3)
    ]
).

