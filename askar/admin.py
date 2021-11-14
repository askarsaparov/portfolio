from django.contrib import admin

from askar.models import Home, About, Profile, Category, Skills, Portfolio, Cantact

admin.site.register(Home)
#About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

#Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]

#Portfolio
admin.site.register(Portfolio)
admin.site.register(Cantact)