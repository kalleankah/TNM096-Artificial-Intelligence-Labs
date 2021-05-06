act(
  go(From, To),
  %, if to is box then lighton else nothing, is this correct ((box(To),switchOn()) ; \+ box(To))
  [connects(shakey, From), \+ connects(shakey, To), \+ ontop(shakey), (connects(From,To);connects(To,From))],
  [connects(shakey, From)],
  [connects(shakey, To)]
).

act(
  push(Box, From, To),
  [connects(shakey, Box), connects(Box, From), \+ connects(b, To), \+ ontop(shakey)],    %Precondistions
  [connects(Box, From), connects(shakey, From)],    %To Delete
  [connects(Box, To), connects(shakey, To)]     %To Add
).

act(
  switchOnLight(Light),
  [ontop(shakey),connects(shakey, Light), \+ switchOn(Light)],    %Precondistions
  [],    %To Delete
  [switchOn(Light)]     %To Add
).

act(
  switchOffLight(Light),
  [ontop(shakey),connects(shakey, Light), switchOn(Light)],    %Precondistions
  [switchOn(Light)],    %To Delete
  []     %To Add
).

act(
  climbUp(Box),
  [\+ ontop(shakey), connects(shakey, Box)],    %Precondistions
  [],    %To Delete
  [ontop(shakey)]     %To Add
).

act(
  climbDown(),
  [ontop(shakey)],    %Precondistions
  [ontop(shakey)],    %To Delete
  []     %To Add
).