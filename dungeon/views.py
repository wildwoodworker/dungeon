from django.shortcuts import render, redirect
from django.http import Http404
from .rooms import getRoomDetails,rooms
from .gameflow import nextRoom

# Create your views here.
def home(request):
    print (request)
    return render(request, 'main/index.html')

def newgame(request):
  if request.method == "POST":
    return  redirect("room")
  else:
    return redirect('home')


# The room method is either sending back room details or 
# analysing the choice specified by the user to select which door or other
# choice presented to the user. A GET request means simply view the room page
# whereas the POST request indicates a choice.
#
# The program expect the following carried over data:
# 
#    backpack: list of string, indicating carried items along the quest/journey
#    roomid: 
#    selected: the choice selected by the user. 
#
def room(request):
  info={}
  if request.method == 'GET':
    if 'roomid' in request.GET:
      info['roomid']=request.GET['roomid']
    else:
      # We default to room 1 if no room is specified in the GET request
      info['roomid']=1

    if 'backpack' in request.GET:
      info['backpack']=request.GET['backpack']
    else:
      info['backpack']=""

    info['room'] = getRoomDetails(str(info['roomid']))
    if info['room'] == None:
      raise Http404("room does not exist")
    
  elif request.method == 'POST':
    selection=request.POST['key']
    backpack=request.POST['backpack']
    currentRoom=request.POST['currentRoom']
    info = nextRoom(currentRoom, backpack, selection)
  
  return render(request, info['room']['template'], info)
