from django.shortcuts import redirect, render
from .models import Recipe
# Create your views here.
def recipes(request):
    if request.method == 'POST':
        r1 = Recipe()
        r1.recipe_name = request.POST['recipe_name']
        r1.recipe_description = request.POST['recipe_description']
        r1.recipe_image = request.FILES.get('recipe_image')
        r1.save()

    recipe_data = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipe_data': recipe_data}) 

def update_recipe(request, id):
    recipe_data = Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe_data.recipe_name = request.POST['recipe_name']
        recipe_data.recipe_description = request.POST['recipe_description']
        recipe_data.recipe_image = request.FILES.get('recipe_image')
        recipe_data.save()    
        return redirect('recipes')
    else:
        return render(request, 'updaterecipe.html', {'recipes': recipe_data})

def delete_recipe(request, id):
    r1 = Recipe.objects.get(id=id)
    r1.delete()
    return redirect('recipes')