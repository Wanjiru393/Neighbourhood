from django.contrib import admin
from .models import neighbourhood,healthservices,Health,notifications,Authorities,Profile


class HealthAdmin(admin.ModelAdmin):
    filter_horizontal =['healthservices']

# Register your models here.
admin.site.register(neighbourhood)
admin.site.register(Health,HealthAdmin)
admin.site.register(healthservices)
admin.site.register(Authorities)
admin.site.register(Profile)
admin.site.register(notifications)