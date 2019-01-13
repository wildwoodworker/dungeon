#
# Game data
#

rooms = {
    'gameover': {
        'id': 'gameover',
        'template': 'main/room.html', 
        'roomPic': 'gameover.jpg',
        'title': 'Gameover',
        'description':'explain why you died', 
        'question':'...',
        'choices': [ {'prompt': 'play again', 'key': 's1'},
                    ],
        },
    '1': {
        'id': '1',
        'template': 'main/room.html', 
        'roomPic': '3doors.jpg',
        'title': 'Cave room 1',
        'description':'this is a dark cave with monters...', 
        'question':'choose a door',
        'choices': [ {'prompt': 'Going to room 2', 'key': 's1'},
                     {'prompt': 'Going to room 2 and taking the chiken', 'key': 's2'},
                     {'prompt': 'test gameover', 'key': 's3'}
                    ],
        # Next room is a list of possible mapping.  This data drives the next step in the game.  
        'actions': [  { 'key':'s1', 'bpr':'', 'newRoom': '2', 'whatsup': 'you are going to room two without chicken'},
                        { 'key':'s2', 'bpr':'', 'newRoom': '2', 'whatsup': 'adding chicken do little ', 'newBackPack':'+chicken'},
                        { 'key':'s3', 'bpr':'', 'newRoom': 'gameover', 'whatsup': 'sorry you were just unlucky' },
                ],
        },
    '2': {
        'id': '2',
        'template': 'main/room.html', 
        'roomPic': '3doors.jpg',
        'title': 'Cave room 2',
        'description':'this is a dark cave with monters...', 
        'question':'choose a door',
        'choices': [ {'prompt': 'Test chicken', 'key': 's1'},
                     {'prompt': 'gameover test', 'key': 's2'},
                    ],
        'actions': [  { 'key':'s1', 'bpr':'', 'newRoom': '1', 'whatsup': 'you are going back to room one gien you have no chicken'},
                        { 'key':'s1', 'bpr':'chicken', 'newRoom': '3', 'whatsup': 'next step given I had chicken'},
                        { 'key':'s2', 'bpr':'', 'newRoom': 'gameover', 'whatsup': 'sorry you were just unlucky' },
                ],
        },
    '3': {
        'id': '3',
        'template': 'main/room.html', 
        'roomPic': '3doors.jpg',
        'title': 'Cave room 3',
        'description':'this is a dark cave with monters...', 
        'question':'choose a door',
        'choices': [ {'prompt': 'Door 1', 'key': 's1'},
                     {'prompt': 'Door 2', 'key': 's2'},
                     {'prompt': 'Door 3', 'key': 's3'}
                    ],
        },
}

def getRoomDetails(roomId):
    return rooms[roomId]