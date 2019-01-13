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
def nextRoom(currentRoomId, backpack, selection):
    # Prepare my return dictionary describing the next room
    # Init with empty dictionary
    info = {}
    # copy existing backpack before potentially modifying
    info['backpack']=backpack[:]

    if (currentRoomId == 'gameover'):
        #  The only possible action from gameover is to start a new game
        #  i.e. redirect to room 1 and empty backpack
        info['roomid']='1'
        info['backpack']=[]
    else:
        # match the next room
        action= getActionFromSelection(currentRoomId, selection, info)
        if action == None:
            raise Http404("error matching action from selection")
        
        # process matching response
        nextRoomId = action.get('newRoom')
        if nextRoomId == None:
            raise Http404("No matching next room")
    
        process_backpack_action(action.get('newBackPack'), info)
        # Copy over the remaining field into the dictionary 
        info['roomid'] = action.get('newRoom')
        info['room']=getRoomDetails(action.get('newRoom'))
        info['whatsup'] = action.get('whatsup')
    return info

def getActionFromSelection(currentRoomId, selection, info):
    bestmatch = {}
    score=0
    # Loop to possibility and find mapping
    roomDetail = getRoomDetails(currentRoomId)
    actions = roomDetail.get('actions')
    if actions == None:
        return None
    for action in actions:
        # Find how close the response is using weight
        lcount=0
        if action['key'] == selection:
            lcount=lcount + 5
            # check the backpack for extra credits
            backpack_rule = action.get('bpr')
            if (backpack_rule != None) and (backpack_rule != ''):
                # we must check if we have the backpack item
                # TODO: code could be extended to check multiple items within the backpack
                if backpack_rule in info['backpack']:
                    lcount = lcount + 5
        if lcount > score:
            # replace our bestmatch action given this one has a higher score
            # and remember the new higher score
            bestmatch = action
            score=lcount
    return bestmatch


def process_backpack_action(rule, info):
    if rule == None:
        # no backpack rule, simply return
        return
    if rule.startswith('+'):
        # we are adding an element to the backpack
        info['backpack'].append(rule[1:])

