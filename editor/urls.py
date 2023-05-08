# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 19:24
# @Author  : AI悦创
# @FileName: urls.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from django.urls import path

from . import views

urlpatterns = [
    path("", views.editor, name="editor"),
    path("upload_code", views.upload_code, name="upload_code")
]