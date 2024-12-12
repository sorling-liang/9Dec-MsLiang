# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
# step1: define the function
def come():
    agent.teleport_to_player()

# step2: connect
player.on_chat("tp", come)

def turn_left():
    agent.turn(LEFT)

def turn_right():
    agent.turn(RIGHT)

player.on_chat("tl", turn_left)
player.on_chat("tr", turn_right)

def forward(steps):
    agent.move(FORWARD, steps)
player.on_chat("fw", forward)

def up(steps):
    agent.move(UP, steps)
player.on_chat("up", up)

def down(steps):
    agent.move(DOWN, steps)
player.on_chat("dn", down)

def back(steps):
    agent.move(BACK, steps)
player.on_chat("bk", back)

def climb():
    agent.move(UP, 1)
    agent.move(FORWARD, 1)

player.on_chat("mv", climb)

def descent():
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("dn", descent)

# day 2
def choptree(tall):
    for count in range(tall):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, tall)
    agent.collect_all()

player.on_chat("chop", choptree)

def dig(steps):
    for count in range(steps):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)

player.on_chat("dc", dig)