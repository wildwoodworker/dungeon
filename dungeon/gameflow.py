from .rooms import getRoomDetails
from django.http import Http404

# This method determine the next step in the game
# input:
#    currentRoom: current room number integer, 1 is the first room, 0 is game over
#    backpack: list of actifacts you are carrying around
#    selected: this is the choice selected by the player. 's1', 's2', 's3'
# output:
#    object with
#       backpack: string
#       room: room details
#    room details information.  Game over is a special room.
def nextRoom(currentRoomId, backpack, selected):
    # Prepare my return dictionary describing the next room
    # Init with empty dictionary
    info = {}

    # insert your logic on which room to go next

    if (currentRoomId != 0):
        if selected == 's1':
            info['room']=getRoomDetails('1')
            info['roomid']=1
        elif selected == 's2':
            info['room']=getRoomDetails('2')
            info['roomid']=1
        elif selected == 's3':
            info['room']=getRoomDetails('3')
            info['roomid']=3
        else:
            raise Http404("Invalid next room")

    info['backpack'] =  backpack + " was:" + str(selected) 
    return info

