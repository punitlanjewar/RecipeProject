from django.shortcuts import redirect, render
from .models import Recipe, User
from django.contrib.auth import authenticate, login
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        user_name = request.POST['txtUsername']
        user_password = request.POST['txtPassword']
        user = authenticate(username=user_name, password=user_password)
        if user is None:
            return render(request, 'login.html', {'Msg': 'Incorrect Credentials'})
        else:
            login(request, user)
            return redirect('recipes')
    else:
        return render(request, 'login.html')    
    
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('txtFirstName')
        last_name = request.POST.get('txtLastName')
        user_name = request.POST.get('txtUsername')
        user_password = request.POST.get('txtPassword')
        if User.objects.filter(username=user_name).exists():
            return render(request, 'register.html', {'Msg': 'Username already taken'})
        else:
            user = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name, 
                username=user_name, 
                password=user_password
                )
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')    


def recipes(request):
    if request.method == 'POST':
        r1 = Recipe()
        r1.recipe_name = request.POST['recipe_name']
        r1.recipe_description = request.POST['recipe_description']
        r1.recipe_image = request.FILES.get('recipe_image')
        r1.save()

    recipe_data = Recipe.objects.all()
    if request.GET.get('SearchBox'):
        recipe_data = recipe_data.filter(recipe_name__icontains = request.GET.get('SearchBox'))
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

