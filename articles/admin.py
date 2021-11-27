from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ScopePosition


class ScopeFormset(BaseInlineFormSet):
    def clean(self):
        t = 0
        for form in self.forms:
            dictcleaned = form.cleaned_data
            print(dictcleaned)
            if not dictcleaned.get('is_main'):
                continue
            elif dictcleaned['is_main']:
                t += 1
        if t == 0:
            raise ValidationError('Выберите хотя бы 1 тег')
        elif t > 1:
            raise ValidationError('Слишком много тегов (оставьте только 1 тег)')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = ScopePosition
    formset = ScopeFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
