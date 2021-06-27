from django.contrib import admin
#モデルからの読み込み
from .models import Grade,Member

#gradeに対する操作権限
admin.site.register(Grade)

#Memberに対する操作権限
admin.site.register(Member)

# Register your models here.
