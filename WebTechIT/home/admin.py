# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import DanhMuc, TinTuc, HashTag, Category, LoaiTin, Images

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(DanhMuc)
admin.site.register(TinTuc)
admin.site.register(HashTag)
admin.site.register(Category, CategoryAdmin)
admin.site.register(LoaiTin)
admin.site.register(Images)
