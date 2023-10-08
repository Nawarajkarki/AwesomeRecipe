from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(RecipePost)
admin.site.register(Ingredient)
admin.site.register(Step)
admin.site.register(RecipeImage)
admin.site.register(Saved)