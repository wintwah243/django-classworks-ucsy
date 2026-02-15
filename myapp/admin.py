from django.contrib import admin
from .models import Student, Store, StudentInfo, StudentDetail, Product

# .....

admin.site.register(Student)
admin.site.register(Store)
admin.site.register(StudentInfo)
admin.site.register(StudentDetail)
admin.site.register(Product)