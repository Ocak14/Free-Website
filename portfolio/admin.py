from django.contrib import admin
from django.shortcuts import render
from .models import About,Contact,Service,Team,Client
from django.utils.html import format_html





@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title","description","img")
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
    from django.db import models


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","phone_number","email","content")
    readonly_fields = ["id"]

    def __str__(self):
        return f"{self.name} {self.email}"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("img","title","description")
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  

# admin.site.register((Team))


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("img",)
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  
 
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("description","img","title")
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  