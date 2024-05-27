from django.contrib import admin

from .models import Article, City, Discipline, Event, Place, Region, User

admin.site.register(City)
admin.site.register(Discipline)
admin.site.register(Region)
admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Article)
admin.site.register(User)
