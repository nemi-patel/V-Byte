from django.contrib import admin
# Register your models here.
from .models  import Teacher,gamecategory,Student,Timeline,Game,Usersregistration,Rules,Payment,Form


admin.site.register(Teacher)
admin.site.register(gamecategory)
admin.site.register(Student)
admin.site.register(Timeline)
admin.site.register(Game)
admin.site.register(Usersregistration)
admin.site.register(Rules)
admin.site.register(Payment)
admin.site.register(Form)





