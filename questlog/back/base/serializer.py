from rest_framework import serializers
from .models import PlayerCharacter,Quest




class PlayerCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCharacter
        fields = '__all__'



class QuestSerializer(serializers.ModelSerializer):
    pc_involved = serializers.PrimaryKeyRelatedField(queryset=PlayerCharacter.objects.all(), many=True, required=True)

    class Meta:
        model = Quest
        fields = ['quest_name', 'description', 'pc_involved', 'is_completed', 'reward']

    def validate_pc_involved(self, value):
        """
        Ensure the pc_involved field contains at least one PlayerCharacter.
        """
        if not value:
            raise serializers.ValidationError("At least one player character must be involved in the quest.")
        return value