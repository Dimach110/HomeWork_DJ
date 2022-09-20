from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
import re


from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        counter = 0
        for form in self.forms:
            res = form.cleaned_data.get('is_main')
            print(res)
            # тут получаем данные по is_main (либо True либо False) отследить 0 и более 1 указания is_main в Scope
            if res:
                print('да')
                counter += 1
                print(counter)
        if counter != 1:
            print('ошибка')
            raise ValidationError('Основной Тэг должен быть указан и должен быть только 1!')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline, ]
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass
