from django.shortcuts import render, redirect
from .models import *

# View to handle displaying and creating recipes
def receipes(request):
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        data = request.POST
        # Retrieve data from the form
        receipe_name = data.get('Rec_name')
        receipe_desc = data.get('Rec_desription')
        receipe_img = request.FILES.get('Rec_img')

        # Create a new recipe object and save it to the database
        Receipe.objects.create(
            Rec_name = receipe_name,
            Rec_desription = receipe_desc,
            Rec_img = receipe_img,
        )

        # Redirect to the recipes page after saving
        return redirect('/receipes')
    
    # Get all recipe objects
    queryset = Receipe.objects.all()
    
    # Filter the queryset if a search term is provided
    if request.GET.get('Search'):
        queryset = queryset.filter(Rec_name__icontains = request.GET.get('Search'))
    
    # Prepare the context dictionary with the queryset
    context = {'Reciepis': queryset}

    # Render the recipes page with the context
    return render(request, 'receipes.html', context)

# View to handle updating a specific recipe
def update_receipe(request, id):
    # Get the recipe object by ID
    queryset = Receipe.objects.get(id=id)
    
    # Prepare the context dictionary with the recipe object
    context = {'Reciepi': queryset}
    
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        data = request.POST
        # Retrieve data from the form
        receipe_name = data.get('Rec_name')
        receipe_desc = data.get('Rec_desription')
        receipe_img = request.FILES.get('Rec_img')

        # Update the recipe object with new data
        queryset.Rec_name = receipe_name
        queryset.Rec_desription = receipe_desc

        # Update the recipe image if a new one is provided
        if receipe_img:
            queryset.Rec_img = receipe_img

        # Save the updated recipe object
        queryset.save()
        
        # Redirect to the recipes page after saving
        return redirect('/receipes')

    # Render the update recipe page with the context
    return render(request, 'update_receipe.html', context)

# View to handle deleting a specific recipe
def delete_receipe(request, id):
    # Get the recipe object by ID
    queryset = Receipe.objects.get(id = id)
    
    # Delete the recipe object
    queryset.delete()
     
    # Redirect to the recipes page after deleting
    return redirect('/receipes')

'''
# Debugging code to print out form data
print(receipe_name)
print(receipe_desc)
print(receipe_img)
print(data)
'''
