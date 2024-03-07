from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

def gracias(request):
    if request.method == 'GET':
        return render(request, 'blogApp/gracias.html')


def home(request):
    if request.method == 'GET':
        print('presentar documento home.html')
        return render(request, 'blogApp/home.html')
    elif request.method == 'POST':
        print('la data recibido es:',request.POST)

# <QueryDict: {'csrfmiddlewaretoken': ['H97knFT1cNaacZCBYNeLK9A8BKUMdjPTuOX1DkQIlOalkx8qHIpaT2c5CzNxiCfc'], 'email': ['dojoFS@gmail.com'], 'password': ['hacking123']}>
        data = request.POST
        email = data['email']
        password = data['password']
        
        print('recibir datos del formulario.html', email, password)

        # return render(request, 'blogApp/gracias.html')
        return redirect('/gracias')






class BlogHome(View):

    def get(self, request):
        return render(request, 'blogApp/blog_home.html')

    def post(self, request):
        print(request.POST)
        return render(request, 'blogApp/blog_home.html')