from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(category)
admin.site.register(Blog)
admin.site.register(user_detail)
admin.site.register(like_blog)
admin.site.register(user_comment)
admin.site.register(message)

