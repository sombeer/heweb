from django.urls import path
from he_admin import views


app_name='he_admin'
urlpatterns = [
    #categories path

    path('',views.index,name='index'),
    path('addproductscategory',views.add_products_category,name='addcategory'),
    path('showcategories',views.ShowCategory,name='showcategories'),
    path('view/<int:id>/',views.ViewCategory,name='viewcategory'),
    path('edit-category/<int:id>/',views.EditCategory,name='editcategory'),
    path('delete-category/<int:id>/',views.DeleteCategory,name='deletecategory'),
    path('status-category/<int:id>/',views.StatusCategory,name='statuscategory'),

    #Products path
    path('addproducts',views.Add_Products,name='addproducts'),
    path('showproducts',views.ShowProducts,name='showproducts'),
    path('view-product/<int:id>/',views.ViewProduct,name='viewproduct'),
    path('edit-product/<int:id>/',views.EditProduct,name='editproduct'),
    path('delete-product/<int:id>/',views.DeleteProduct,name='deleteproduct'),
    path('status-product/<int:id>/',views.StatusProduct,name='statusproduct'),
    
]