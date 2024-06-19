from django.db import models

# Define the Receipe model
class Receipe(models.Model):
    # Recipe name with a maximum length of 100 characters
    Rec_name = models.CharField(max_length=100)
    
    # Detailed recipe description
    Rec_desription = models.TextField()
    
    # Image of the recipe, stored in the 'receipes' directory
    Rec_img = models.ImageField(upload_to="receipes")
