from django.urls import path
from carapp import views


urlpatterns=[
    path('index3/',views.index3,name="index3"),
    path('brandzz/',views.brandzz,name="brandzz"),
    path('brandsave/',views.brandsave,name="brandsave"),
    path('dspbrand/',views.dspbrand,name="dspbrand"),
    path('carss/',views.carss,name="carss"),
    path('carssave/',views.carssave,name="carssave"),
    path('dspcar/',views.dspcar,name="dspcar"),
    path('',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('editbrandpage/<int:dataid>/',views.editbrandpage,name="editbrandpage"),
    path('updatebrand/<int:dataid>/',views.updatebrand,name="updatebrand"),
    path('deletebrand/<int:dataid>/',views.deletebrand,name="deletebrand"),
    path('editcarpage/<int:productid>/',views.editcarpage,name="editcarpage"),
    path('updatecar/<int:productid>/',views.updatecar,name="updatecar"),
    path('deletecars/<int:productid>/',views.deletecars,name="deletecars"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecontact/<int:contactid>/', views.deletecontact, name="deletecontact"),
    path('dspcart/', views.dspcart, name="dspcart"),
    path('dspreview/', views.dspreview, name="dspreview"),
    path('dspcarsell/', views.dspcarsell, name="dspcarsell"),
    path('custrating/', views.custrating, name="custrating"),
    path('reviewsave/', views.reviewsave, name="reviewsave"),
    path('displogss/', views.displogss, name="displogss"),
    path('cartdelete/<int:cartid>/', views.cartdelete, name="cartdelete"),
    path('reviewdelete/<int:revwid>/', views.reviewdelete, name="reviewdelete"),
    path('carselldelete/<int:carsellid>/', views.carselldelete, name="carselldelete"),
    path('deletelog/<int:loginnid>/', views.deletelog, name="deletelog"),

]