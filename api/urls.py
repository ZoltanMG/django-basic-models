from django.urls import path
from .views import RecipeView


urlpatterns = [
    path('recipe/', RecipeView.as_view(), name='recipes_list'),
    path('recipe/<int:id>/', RecipeView.as_view(), name='recipe_process')
]