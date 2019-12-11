from django.contrib import admin

# Register your models here.
from goods.models import Goodimage, Good, Category

admin.site.register(Category)
admin.site.register(Good)
admin.site.register(Goodimage)