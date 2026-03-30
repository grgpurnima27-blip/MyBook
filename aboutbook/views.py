from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book
from .forms import create, EditPost

# Home / list all books
def home(request):
    books = Book.objects.all()
    return render(request, 'aboutbook/home.html', {'books': books})

# Detail page
def detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'aboutbook/detail.html', {'book': book})

# Add book
def add(request):
    form = create()
    if request.method == "POST":
        form = create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully! ✅")
            return redirect('book_list')
    return render(request, 'aboutbook/create.html', {'form': form})

# Edit book
def edit(request, id):
    book = get_object_or_404(Book, id=id)
    form = EditPost(instance=book)
    if request.method == "POST":
        form = EditPost(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully! ✏️")
            return redirect('book_list')
    return render(request, 'aboutbook/edit.html', {'form': form})

# Delete book
def delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully! 🗑️")
        return redirect('book_list')
    return render(request, 'aboutbook/delete.html', {'book': book})