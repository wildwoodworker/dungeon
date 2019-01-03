from django.shortcuts import render, redirect
from django.http import Http404
from .gamedata import getRoomDetails,rooms
from .gameflow import nextRoom
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.
def home(request):
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
    # To jump directly to a room, just do /room?roomid=3&backpack=whatyouwant

    if 'roomid' in request.GET:
      info['roomid']=request.GET['roomid']
    else:
      # We default to room 1 if no room is specified in the GET request
      # and empty backpack
      info['roomid']='1'

    if 'backpack' in request.GET:
      backpackStr = request.GET['backpack']
      if backpackStr != "":
        backpack=backpackStr.split(',')
      else:
        backpack=[]  
      info['backpack']=backpack
    else:
      info['backpack']=[]

    info['room'] = getRoomDetails(info['roomid'])
    if info['room'] == None:
      raise Http404("Room details does not exist")
    return render(request, info['room']['template'], info)

  elif request.method == 'POST':
    #
    # Collect POST attributes 
    #
    user_selection=request.POST['key']
    backpackStr=request.POST['backpack']
    if backpackStr != "":
      backpack=backpackStr.split(',')
    else:
      backpack=[]
    currentRoom=request.POST['currentRoom']
    # 
    # Figure out where to go nect
    #
    info = nextRoom(currentRoom, backpack, user_selection)
    # 
    # We have two choices here.  Redirect to the GET request or render the page directly
    # The redirect is easier fro debugging.  
    # Option 1: render:
    #    return render(request, info['room']['template'], info)
    # Option 2: redirect to GET request with the right parameters for the next page
    base_url = reverse('room')
    query_string =  urlencode({'roomid': info['roomid'], 'backpack': ','.join(info['backpack']) })
    url = '{}?{}'.format(base_url, query_string)  # /room/?roomid=4&backpack=chicken
    return redirect(url)  


