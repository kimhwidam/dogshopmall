from django.db import models
from user.models import User

# Create your models here.
class Color(models.Model):
    color_id = models.CharField(primary_key=True,max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'my_dog_color'

class Size(models.Model):
    size_id = models.CharField(primary_key=True,max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'my_dog_size'

class State(models.Model):
    state_id = models.CharField(primary_key=True,max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'my_dog_state'

class Age(models.Model):
    age_id = models.CharField(primary_key=True,max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'my_dog_age'

class Species(models.Model):
    species_id = models.CharField(primary_key=True,max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'my_dog_species'

class Dog(models.Model):
    dog_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    age_id = models.ForeignKey(Age, on_delete=models.CASCADE)
    species_id = models.ForeignKey(Species, on_delete=models.CASCADE)

    class Meta:
        db_table = 'my_dog'