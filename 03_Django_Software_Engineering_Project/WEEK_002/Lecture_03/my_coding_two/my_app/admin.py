from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.studentModel)

# abstract inherited classes
admin.site.register(models.studentInfoModel)
admin.site.register(models.teacherInfoModel)
# admin.site.register(models.studentModel,models.studentInfoModel,models.teacherInfoModel)

# multiple inheritance classes
@admin.register(models.employeeModel)
class employeeModelAdmin(admin.ModelAdmin):
    list_display =['name','id','address','designation']
@admin.register(models.managerModel)
class managerModelAdmin(admin.ModelAdmin):
    list_display =['name','id','address','designation','take_hire','take_interview','take_promotion']

# proxy inherited classes
@admin.register(models.FriendModel)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'section', 'attendance', 'hw']

@admin.register(models.MeModel)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'section', 'attendance', 'hw']


# one_to_one rel
@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age','city','email']
@admin.register(models.Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ['person_user','passport_type','passport_number','page','validity','regional_office']


# one to many rel
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','id','address','section']
@admin.register(models.Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['student_user','book_name','who_take_book']


# many to many rel
@admin.register(models.Studentinfo)

class StudentinfoModelAdmin(admin.ModelAdmin):
    list_display = ['name','id','address','cur_class','teacher_list']

@admin.register(models.Teacherinfo)
class TeacherinfoModelAdmin(admin.ModelAdmin):
    list_display = ['name','subject','address','salary','phone','student_list']
