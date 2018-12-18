from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def nextroom(request):
    # extract necessary arguments
    room = request.GET['current_room']
    choice = request.GET['choice']

    ## Call a method to determine the next room
    # extract the room template name
    # create room context info and pass it to render
    room_details = newRoomDetails(room, choice)    
    # render(request,'main/room.html')

    return render(request, room_details['template'], room_details)


def newRoomDetails(currentRoom, choice):
  newRoom=int(currentRoom)
  if (newRoom > 0):
    newRoom=newRoom+1
  # create an object for room details
  # you can add all sort of logic to determine the next room template
  return { 'template': 'main/room.html', 
            'roomId': str(newRoom), 
            'title':'Cave '+ str(newRoom), 
            'description':'this is a dark cave with monters...', 
            'question':'choose a door', 
            'roomPic': '3doors.jpg'}
