from django.contrib import admin
from neekap.models import Blog, Category, SlideShow, StatsFactor, Logo, trial
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

# class HomepageAdmin(admin.ModelAdmin):
# 	label = 'Homepage'


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(trial)
# admin.site.register(Homepage, HomepageAdmin)
# admin.site.register(Mission)
# admin.site.register(StatsFactor)
# admin.site.register(Logo)
