from django.db import models

# Create your models here.



class PlayerCharacter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quest(models.Model):
    quest_name = models.CharField(max_length=50, primary_key=True, null=False, default = "", blank=False)
    description= models.CharField(max_length=200, null=False, default = "", blank=False)
    pc_involved = models.ManyToManyField(PlayerCharacter, default='[]')
    is_completed = models.BooleanField(default=False, null=False, blank=False)
    reward = models.CharField(max_length=100, null=False, default = "check with the DM",blank=False)

    def __str__(self):
        return self.quest_name
    


class QuestTEST(models.Model):
    quest_name = models.CharField(max_length=50, primary_key=True, null=False, default = "", blank=False)
    description= models.CharField(max_length=200, null=False, default = "", blank=False)
    pc_involved = models.TextField(default="[]")
    is_completed = models.BooleanField(default=False, null=False, blank=False)
    reward = models.CharField(max_length=100, null=False, default = "check with the DM",blank=False)

    def __str__(self):
        return self.quest_name




    # @property
    # def pc_involved(self):
    #     # Deserialize the JSON data to Python list
    #     ids = json.loads(self.pc_involved_ids)
    #     return PlayerCharacter.objects.filter(id__in=ids)

    # @pc_involved.setter
    # def pc_involved(self, pcs):
    #     # Serialize the list of PlayerCharacter IDs to JSON
    #     ids = [pc.id for pc in pcs]
    #     self.pc_involved_ids = json.dumps(ids)
