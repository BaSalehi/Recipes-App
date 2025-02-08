from rest_framework.views import APIView
from rest_framework.response import Response
from recipe_app.models import Recipe
from recipe_app.api.serializers import RecipeSerializer


class RecipeListAV(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    
