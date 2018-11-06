from django.contrib import admin
from .models import (User, Subject, Quiz, Question, Answer, Student,
                     TakenQuiz, StudentAnswer, )
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)
