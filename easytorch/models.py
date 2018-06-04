from django.db import models

class Easy(models.Model):
    type=models.CharField(max_length=20)
    neurons=models.IntegerField()
    layers_neurons=models.IntegerField()
    input=models.IntegerField()
    output=models.IntegerField()

    def __str__(self):
        return self.type
