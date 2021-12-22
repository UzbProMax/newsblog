from django.contrib import admin
from . import models

myModels = [models.Blog, models.Category, models.Tags]
admin.site.register(myModels)