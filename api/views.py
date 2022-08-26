from types import MethodDescriptorType
from urllib import response
from django.views import View
from .models import Recipe
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class RecipeView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            recipe = list(Recipe.objects.filter(id=id).values())
            reponse = {"recipe": recipe}
            return JsonResponse(reponse)

        recipes = list(Recipe.objects.values())
        reponse = {"recipes": recipes}
        return JsonResponse(reponse, safe=False)

    def post(self, request):
        json_data = json.loads(request.body)
        Recipe.objects.create(
            name_recipe=json_data['name_recipe'],
            favorite=json_data['favorite'],
            recipe_owner=json_data['recipe_owner'],
            color_card=json_data['color_card']
        )
        response = {'message': "success"}
        return JsonResponse(response)

