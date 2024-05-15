from django.shortcuts import render

# Create your views here.


def HomeView(request) :
    
    print("HomePage Run Successfully !!")
    
    return render(request, "index.html")


def AboutView(request) :
    print("About Page Run Successfully !!")
    return render(request, "about.html")
    

def ShopView(request) :
    print("Shop Page Run Successfully !!")
    return render(request, "shop.html")

def ServicesView(request) :
    print("Services Page Run Successfully !!")
    return render(request, "services.html")


def BlogView(request) :
    print("Blog Page Run Successfully !!")
    return render(request, "blog.html")

def ContactView(request) :
    print("Contact Page Run Successfully !!")
    return render(request, "contact.html")

def CartView(request) :
    print("Cart Page Run Successfully !!")
    return render(request, "cart.html")


