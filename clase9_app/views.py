from django.shortcuts import redirect, render

from clase9_app.forms import ProductoForm
from clase9_app.models import Producto

# Create your views here.
def lista_objetos(request):
    objetos = Producto.objects.all()
    print(list(objetos))
    print(objetos.values())
    print(list(objetos.values()))
    return render(request, 'lista_objetos.html', {'objetos': objetos})

def crear_objeto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_objetos")
    else:
        form = ProductoForm()
    
    return render(request, "crear_objeto.html", {"form": form})