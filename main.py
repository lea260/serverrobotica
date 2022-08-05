#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!
from pybricks.hubs import EV3Brick
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks.tools import wait, StopWatch

ev3 = EV3Brick()
ev3.speaker.beep(3000, 0.5)
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
#print('waiting for connection...')
server.wait_for_connection()
#print('connected!')
ev3.screen.print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.
mbox.wait()
#print(mbox.read())
mbox.send('hello to you!')
ev3.screen.print(mbox.read())
wait(2000)