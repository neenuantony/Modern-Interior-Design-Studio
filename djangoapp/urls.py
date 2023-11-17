from django.urls import path
from .views import *

urlpatterns=[
    path('first/',first),
    path("second/",second),
    path("third/",third),
    path('four/',fourth),
    path('reg/',registration),
    path('login/',login),
    path('home/',index),
    path('fileupload/',file_upload),
    path('employee_register/',employee_registration),
    path('search/',emp_search),
    path('uploads/',uploadings),
    path('sample/',select_checkbox),
    path('display/',display),
    path('filedisplay/',filedisplay),
    path('upload_dis/',uploadsdisplay),
    path('updatedata/<int:id>',update_data),
    path('empdisplay/',emp_display),
    path('emp_update/<int:id>',emp_update),
    path('file_edit/<int:id>',file_edit),
    path('edit/<int:id>',edit_uploads),
    path('deletedata/<int:id>',delete_profile),
    path('emp_delete/<int:id>',delete_emp),
    path('file_delete/<int:id>',delete_file),
    path('delete/<int:id>',delete_uploads),
    path('authuserregister/',userregistration),
    path('authuserreg/',userReg),
    path('authlogin/',user_login),
    path('product_details/',product_api.as_view(),name='product_details'),
    path('media_files',media_file_api.as_view(),name='media_files')
]