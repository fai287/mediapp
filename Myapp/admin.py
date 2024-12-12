from django.contrib import admin

# Register your models here.


## this is for registering the models in the admin page for them to be displayed

from.models import Member

from Myapp.models import Member, Product, Appointment,Contact,User,ImageModel



admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(ImageModel)


