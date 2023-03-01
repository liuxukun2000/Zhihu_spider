from django.contrib import admin

import zhihu


@admin.register(zhihu.models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "area"]
    search_fields = ["area"]

@admin.register(zhihu.models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "answer_count"]
    # search_fields = ["area"]

@admin.register(zhihu.models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "comment_count"]
    # search_fields = ["area"]

@admin.register(zhihu.models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "content"]
    # search_fields = ["area"]