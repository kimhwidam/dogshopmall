from django.contrib import admin
from dog.models import Dog, Color, Size, Species, Age, State

# Register your models here.
admin.site.register(Dog)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Species)
admin.site.register(Age)
admin.site.register(State)