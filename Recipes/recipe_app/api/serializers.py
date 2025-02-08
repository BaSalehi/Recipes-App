from rest_framework import serializers

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    ingredients = serializers.CharField()
    instructions = serializers.CharField()