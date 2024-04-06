from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PlayerCharacter,Quest
from .serializer import PlayerCharacterSerializer,QuestSerializer
from .forms import QuestForm
@api_view(['GET'])
def index(req):
    return Response('hello')


@api_view(['GET','POST','DELETE','PUT','PATCH'])
def Pc(req, id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_player=PlayerCharacter.objects.get(id=id)
                return Response (PlayerCharacterSerializer(temp_player,many=False).data)
            except PlayerCharacter.DoesNotExist:
                return Response ("GET not found")
        all_players=PlayerCharacterSerializer(PlayerCharacter.objects.all(),many=True).data
        return Response ( all_players)
    # _________________________________________________
    if req.method =='POST':
        plr_serializer = PlayerCharacterSerializer(data=req.data)
        if plr_serializer.is_valid():
            plr_serializer.save()
            return Response ("new player is born")
        else:
            return Response (plr_serializer.errors)
        
        # _________________________________________________
    if req.method =='DELETE':
        try:
            temp_player=PlayerCharacter.objects.get(id=id)
        except PlayerCharacter.DoesNotExist:
            return Response ("DEL not found")    
       
        temp_player.delete()
        return Response ("del...")
    # _________________________________________________
    if req.method =='PUT':
        try:
            temp_player=PlayerCharacter.objects.get(id=id)
        except PlayerCharacter.DoesNotExist:
            return Response (" PUT not found")
       
        ser = PlayerCharacterSerializer(data=req.data)
        old_player = PlayerCharacter.objects.get(id=id)
        res = ser.update(old_player, req.data)
        return Response(res)


@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def quests(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                quest = Quest.objects.get(id=id)
                serializer = QuestSerializer(quest, many=False)
                return Response(serializer.data)
            except Quest.DoesNotExist:
                return Response({"message": "Quest not found"}, status=404)
        quests = Quest.objects.all()
        serializer = QuestSerializer(quests, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = QuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Quest created successfully"}, status=201)
        return Response(serializer.errors, status=400)

    if request.method in ['PUT', 'PATCH']:
        if id is None:
            return Response({"message": "Method requires an 'id' parameter"}, status=400)
        try:
            quest = Quest.objects.get(id=id)
        except Quest.DoesNotExist:
            return Response({"message": "Quest not found"}, status=404)
        
        # For PATCH requests, use partial=True to allow partial updates
        serializer = QuestSerializer(quest, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Quest updated successfully"})
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        if id is None:
            return Response({"message": "Method requires an 'id' parameter"}, status=400)
        try:
            quest = Quest.objects.get(id=id)
        except Quest.DoesNotExist:
            return Response({"message": "Quest not found"}, status=404)
        quest.delete()
        return Response({"message": "Quest deleted successfully"})

    # Fallback for unsupported methods
    return Response({"message": "Method not supported"}, status=405)


