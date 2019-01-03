from .gamedata import getRoomDetails
from django.http import Http404

# This method determines the next room within the game.  It also control what you add or remove to your
# packback.
#
# input:
#    currentRoomId: String of the current room number
#    backpack: List of string
#    selected: String this is the choice selected by the player. 's1', 's2', 's3', s4...
#
# output:
#    Dictionary with following keys
#       roomid: next room identifier string
#       backpack: list of string
#       room: room details
#
def nextRoom(currentRoomId, backpack, selected):
    # Prepare my return dictionary describing the next room
    # Init with empty dictionary
    info = {}
    # copy existing backpack before modifying
    info['backpack']=backpack[:]

    # insert your logic on which room to go next

    if (currentRoomId != 'gameover'):
        if selected == 's1':
            info['roomid']='1'
            info['room']=getRoomDetails('1')
        elif selected == 's2':
            info['roomid']='2'
            info['room']=getRoomDetails('2')
        elif selected == 's3':
            info['roomid']='gameover'  # game over
            info['room']=getRoomDetails('gameover')
        else:
            raise Http404("Invalid next room")

        # replace by your own logic on how to modify the backpack list
        info['backpack'].append(str(selected)) 
    else:
        # this is the action from the gameover page - i.e. start a new game
        # Redirect to room 1 and empty backpack
        info['roomid']='1'
        info['backpack']=[]

    return info

