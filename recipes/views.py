from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm  # Create this form in Step 5

def recipe_list(request):
    category = request.GET.get('category')  # Get the selected category from the form
    if category:
        recipes = Recipe.objects.filter(meal_type__iexact=category)  # Filter recipes by category
    else:
        recipes = Recipe.objects.all()  # Show all recipes if no category is selected
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

def recipe_update(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})

def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})

def meal_planner(request):
    return render(request, 'meal_planner.html')

def filter_recipes(request):
    query = request.GET.get('ingredient')
    recipes = Recipe.objects.filter(ingredients__icontains=query) if query else Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})
