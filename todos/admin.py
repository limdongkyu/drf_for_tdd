from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "done", "date_created")
    list_filter = ("done", "date_created")


admin.site.register(Todo, TodoAdmin)

