from django.contrib import admin


class ContentAdmin(admin.ModelAdmin):
    search_fields = ['title', 'abstract', 'body', 'slug',]
    list_display = ['title', 'slug', 'is_published', 'pub_date',]
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/javascripts/tinymce_setup.js',
        ]
