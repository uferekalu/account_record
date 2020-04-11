from django.db import models

# Create your models here.
class Mechanical_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Electrical_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Civil_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Computer_Science_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Comp_Engr_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Pharmaceutical_Tech_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Science_Lab_Tech_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Food_Tech_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Dispensary_and_Opticiary_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']

class Agric_Engr_Dept(models.Model):
    added_date = models.DateTimeField()
    name_of_students = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.name_of_students)
    
    class Meta:
        ordering = ['name_of_students']