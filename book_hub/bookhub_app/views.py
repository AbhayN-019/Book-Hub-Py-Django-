from django.shortcuts import render
from bookhub_app.models import Book
from django.contrib import messages
from bookhub_app.forms import BookForm
from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
# Create your views here.

def welcome(request):
    return render(request,'WelcomeTo.html')

def book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Book Details Added Successfully')
            form = BookForm()
            return redirect('book_list')
        
        else :
            messages.error(request,'Something Went Wrong')

    else :
        form = BookForm()

    return render(request,'Book_form.html',{'form' : form})

def book_list(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{'books' : books})

def single_book_view(request,id):
    book = get_object_or_404(Book,id=id)
    return render(request,'single_book.html',{'book':book})

def update_book_view(request,id):

    book = get_object_or_404(Book,id=id)

    if request.method == 'POST':
        update_book = BookForm(request.POST,request.FILES,instance=book)

        if update_book.is_valid():
            update_book.save()
            messages.success(request,"Updated Book Successfully!!")
            return redirect('book_list')
        else:
            messages.error(request,'Please provide valid book deatils')
    else:
        update_book = BookForm(instance=book)
    return render(request,'update_book.html',{'update_book':update_book})

def delete_book(request, id):
    if request.method == "POST":
        book = Book.objects.filter(id=id).first()
        if book:
            book.delete()
            messages.success(request, "Book deleted successfully.")
        else:
            messages.error(request, "Book not found.")
    else:   
        messages.error(request, "Invalid request.")
    return redirect('book_list')