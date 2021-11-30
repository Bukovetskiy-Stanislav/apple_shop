from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from .models import Category, Ipad, Iphone, MacBook, Product
# Register your models here.



class MacBookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='macbook'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class IphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='iphone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class IpadAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='ipad'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(MacBook,MacBookAdmin)
admin.site.register(Iphone,IphoneAdmin)
admin.site.register(Ipad,IpadAdmin)