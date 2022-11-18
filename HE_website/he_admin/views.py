import os
from ast import Delete

from django.contrib import messages
from django.http import Http404
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)

from .forms import AddProductForm, ProductApplicationForm
from .models import ProductApplication, ProductCategory, Products

# Create your views here.

def index(request):
    messages.success(request,"your message has been sent")
    return render(request,'index.html')

# add product category

def add_products_category(request):
    #check_category=Product_Category.objects.values('category')  -> get all data from category coloumn  as key/value pairs
    #check_category=Product_Category.objects.values_list('category') -> get all data from category coloumn  as value pairs
  
    if request.method=="POST":
        category = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = category.upper()
        

        # this will return a tuple of root and extension
        split_tup = os.path.splitext(str(image))
        # extract the file name and extension   
        file_name = split_tup[0]
        file_extension = split_tup[1].lower()
                
       #for image format check
       # image_open=Image.open(image)
       # image_format=image_open.format

        #check category is exist or not
        check_category = ProductCategory.objects.filter(category=category) 
        if check_category:
         unique_error= {
            "error":"Category already Exist",
         }         
         return render(request,'add_product_category.html',unique_error)

         #check image format
        if (str(file_extension) != '.jpeg') and (str(file_extension) != '.jpg') and (str(file_extension) != '.png'):
            image_error={
                "image_error":"Only jpeg,jpg and png images are allowed, you have {} file".format(file_extension)
            }
            #print(file_extension)
            return render(request,'add_product_category.html',image_error)

            

        product_category = ProductCategory(category=category,description=description,category_image=image)
        product_category.save()
        #print(file_extension)
        messages.success(request,"Your category has been added!")
        return redirect('/showcategories') 

    return render(request,'add_product_category.html')
#show all categories
def ShowCategory(request):
    categories = ProductCategory.objects.all()
    return render(request,"show_category.html",{"categories":categories})

#View categories
def ViewCategory(request,id):
    try:
        category=ProductCategory.objects.get(id=id)
    except:
        raise Http404('category does not exist')
    return render(request,"viewcategory.html",{"category":category})

#Update category
def EditCategory(request,id):
    category = ProductCategory.objects.get(id=id) 
    if request.method == 'POST':
        if len(request.FILES)!=0:
            if len(category.category_image) > 0:
                os.remove(category.category_image.path)
            category.category_image = request.FILES['image']
        category.category           = request.POST.get('category').upper()
        category.description        = request.POST.get('description')
        category.save()
        messages.success(request,'category update successfully')
        return redirect('/showcategories')
    return render(request,'update-category.html',{'edit':category})

# Delete category
def DeleteCategory(request,id):
    delete_category = ProductCategory.objects.get(id=id) 
    if len(delete_category.category_image)>0:
        os.remove(delete_category.category_image.path)
    delete_category.delete()
    messages.success(request,'Category Deleted Successfully')
    return redirect('/showcategories')  

#status enable/disable category
def StatusCategory(request,id):
    category = ProductCategory.objects.get(id=id)

    if category.status:
        category.status = False
        category.save()
    else:
        category.status = True
        category.save()
    return redirect('/showcategories')

# Products add    
def Add_Products(request):
    if request.method=='POST':
        productform = AddProductForm(request.POST, request.FILES)
        if productform.is_valid():
            """     category        = productform.cleaned_data['category'].upper()
            product_name    = productform.cleaned_data['product_name']
            Image_alt       = productform.cleaned_data['Image_alt']
            image           = productform.cleaned_data['image'] """
            product = productform.save(commit=False)
            product.save()
            messages.success(request,"Product has been added")
            return HttpResponseRedirect('/showproducts')
    else:
        productform = AddProductForm()
    return render(request,'add_products.html',{'form':productform})

#show products
def ShowProducts(request):
    products = Products.objects.all()
    return render(request,"show-products.html",{'products':products})

#view product
def ViewProduct(request,id):
    product = get_object_or_404(Products,id=id)
    print(product)
    return render(request,"viewproduct.html",{'product':product})

#update product
def EditProduct(request,id):
    product=Products.objects.get(id=id)
    productform = AddProductForm(instance=product)
    if request.method == "POST":
        if len(request.FILES)!=0:
                if len(product.image)>0:
                     print(product.image.path)
                     os.remove(product.image.path)
        productform = AddProductForm(request.POST,request.FILES,instance=product)
        if productform.is_valid():
            product=productform.save(commit=False)
            product.save()
            messages.success(request,"product update successfully")
            return HttpResponseRedirect('/showproducts')  
    return render(request,'update-product.html',{'product':productform})

# permanent delete product
def DeleteProduct(request,id):
    deleteproduct = Products.objects.get(id=id)
    if len(deleteproduct.image)>0:
        os.remove(deleteproduct.image.path)
    deleteproduct.delete()
    messages.success(request,'Product deleted successfully')
    return redirect('/showproducts')
# enable/disable product
def StatusProduct(request,id):
    status = Products.objects.get(id=id)
    if status.status:
        status.status=False
        status.save()
    else:
        status.status = True
        status.save()
    return redirect('/showproducts')

# projects
def projects(request):
    if request.method == "POST":
        form = ProductApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            Form = form.save(commit=False)
            Form.save()
            messages.success(request,'Product application has been added')
            return HttpResponseRedirect('/project')
    else:
        form = ProductApplicationForm()   
    return render(request,'projects.html',{'form':form})