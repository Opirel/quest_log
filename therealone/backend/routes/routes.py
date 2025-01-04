from fastapi import APIRouter, HTTPException, status
from models.QuestModel import QuestMD
from database import Quests

router = APIRouter()

@router.get('/hello')
async def root():
    return {'message': 'hello world'}

# @router.post('/', response_model=QuestMD)
# async def create_quest():

#         QuestName=QuestName
#         QuestDescription= QuestDescription
#         Questreward=Questreward
#         # CharactersInvolved: list[str]
#         # QuestCompleted: bool
#         return {"message": QuestMD, "message":"from back"}


# @router.post('/', response_model=QuestMD)
# async def create_quest(quest: QuestMD):
#     # Logic to handle quest creation
#     return {
#         "QuestName": quest.QuestName,
#         "QuestDescription": quest.QuestDescription,
#         "Questreward": quest.Questreward,
#         "message": "Quest successfully created"
#     }

@router.post('/create', response_model=QuestMD)
async def create_quest(quest_input: QuestMD):
    # Logic to handle quest creation
  try:
        quest = Quests(**quest_input.dict())
        await quest.insert()
        return await quest.get(session.id)
    except Exception as e:
        logging.error(f"Failed to create session: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {




        "QuestName": quest.QuestName,
        "QuestDescription": quest.QuestDescription,
        "QuestReward": quest.QuestReward,
        "CharactersInvolved": quest.CharactersInvolved,
        "QuestCompleted": quest.QuestCompleted,
        "message": QuestMD, "message":"from back"
    }
        