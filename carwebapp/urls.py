from django.urls import path
from carwebapp import views


urlpatterns=[
    path('homePage/',views.homePage,name="homePage"),
    path('procarss/<cat_name>/',views.procarss,name="procarss"),
    path('singlecar/<int:dataid>/',views.singlecar,name="singlecar"),
    path('checkoutSave/',views.checkoutSave,name="checkoutSave"),
    path('contactssave/',views.contactssave,name="contactssave"),
    path('restrform/', views.restrform, name="restrform"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('usrlgn/', views.usrlgn, name="usrlgn"),
    path('logoutt/', views.logoutt, name="logoutt"),
    path('search/', views.search_results, name='search_results'),
    path('carsell/', views.carsell, name='carsell'),
    path('carsellsave/', views.carsellsave, name='carsellsave'),

]