from django.contrib import admin
from .models import Driver, StoreSequence, ConsumerSequence
# Register your models here
admin.site.register(Driver)
admin.site.register(StoreSequence)
admin.site.register(ConsumerSequence)