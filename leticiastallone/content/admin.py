from django.contrib import admin


class ContentAdmin(admin.ModelAdmin):
    search_fields = ['title', 'abstract', 'body', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]
