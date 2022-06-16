from django.db import models

class Equation(models.Model):
    title = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    def __str__(self):
        return self.title

class Example(models.Model):
    equation = models.ForeignKey(Equation,related_name="examples", null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    question = models.CharField(max_length=500)
    solution = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    def __str__(self):
        return self.title
