from django.shortcuts import render
from .models import Book
from .forms import create
# Create your views here.
def home(request):  # show all the records
    book= Book.objects.all()
    context = {
        'books' : book
    }
    return render(request,'aboutbook/home.html',context)

def detail(request,id): # viwe detail of book by an id
    book = Book.objects.get(id=id)
    context ={
        'book' : book
    }
    return render(request, 'aboutbook/detail.html',context)

def add(request):
    form = create()

    if request.method == "POST":
        form = create (data=request.POST)
        if form.is_valid():
            form.save()
        
    context ={
        'form' : form
        }

    return render(request, 'aboutbook/create.html', context)
    

