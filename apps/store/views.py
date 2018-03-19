from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

# '/' OR '/amadon'
def index(request):
    context = {
        'items': [
            {'name': 'Dojo T-shirt', 'price': 19.99},
            {'name': 'Dojo Sweater', 'price': 29.99},
            {'name': 'Dojo Cup', 'price': 4.99},
            {'name': 'Algorithm Book', 'price': 49.99}
        ]
    }
    return render(request,'store/index.html', context)


# '/amadon/checkout'
def checkout(request):
    return render(request,'store/checkout.html')


# '/amadon/buy', handles POST data and redirects to '/amadon/checkout'
def buy(request):
    if 'total_spent' not in request.session:
        request.session['total_spent'] = 0.0
    if 'total_items' not in request.session:
        request.session['total_items'] = 0

    charge = float(request.POST['price']) * float(request.POST['quantity'])
    request.session['charge'] = charge
    request.session['total_spent'] += charge
    request.session['total_items'] += int(request.POST['quantity'])

    return redirect('/amadon/checkout')