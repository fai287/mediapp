from django.db import models

# Create your models here.

#saving the data in the database

class Member(models.Model):
    fullname = models.CharField(max_length=255)#this is for chracters such as letter
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    yob = models.DateField()


    def __str__(self):#ths is string representation of the class which now returns the fullname,email and bla blas blas
        return self.fullname
        return self.email
        return self.age
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.name
        return self.price


from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date = models.DateTimeField()
    #department = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255)
    message = models.TextField()
    department = models.CharField(max_length=255, null=True, blank=True, default='General')

   

    def __str__(self):
        return f"Appointment for {self.name} with Dr. {self.doctor} on {self.date}"


class Contact(models.Model):##this is the form for the contact page
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()


    def __str__(self):
        return f"Contact from {self.name} with email {self.email}, subject {self.subject}, and message: {self.message}"


#creating the model for the registration form 
#its all about posting values to the database

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"name: {self.name}, username: {self.username}, password: {self.password}"



class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title


