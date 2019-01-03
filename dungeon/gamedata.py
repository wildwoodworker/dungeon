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
        'choices': [ {'prompt': 'Door 1 data drive', 'key': 's1'},
                     {'prompt': 'Door 2 running', 'key': 's2'},
                     {'prompt': 'Door 3 bozo', 'key': 's3'}
                    ],
        },
    '2': {
        'id': '2',
        'template': 'main/room.html', 
        'roomPic': '3doors.jpg',
        'title': 'Cave room 2',
        'description':'this is a dark cave with monters...', 
        'question':'choose a door',
        'choices': [ {'prompt': 'Door 1 from room 2', 'key': 's1'},
                     {'prompt': 'Door 2 running', 'key': 's2'},
                     {'prompt': 'Door 3 bozo', 'key': 's3'}
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