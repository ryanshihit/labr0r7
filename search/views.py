# -*- coding: utf-8 -*-
#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from OperateDB import *
# Create your views here.

def index(request):
    bookinfo = read_book()
    books=[]
    for row in bookinfo:
        node1=row[1]
        node2=search_author_by_id(str(row[2]))[1]
        node3=row[5]
        newnode=node1,node2,node3
        books.append(newnode)
    return render_to_response('indexdemo.html',{'books':books})

def addauthorpre(request):
    return render(request, 'addauthor.html')

def addauthor(request):
    try:
        author = getauthormaxnum()[0]+1
        name = request.GET ['name']
        age = request.GET['age']
        country = request.GET['country']
        author=int(author)
        age=int(age)
        print (author,name,age,country)
        k=write_author((author,name,age,country))
        if k:
            return HttpResponseRedirect('/showauthor')
        else:
            return render(request, 'error.html')
    except:
        return render(request, 'error.html')

def addbookpre(request):
    return render(request, 'addbook.html')

def addbook(request):
    try:
        isbn = request.GET['isbn']
        title = request.GET ['title']
        author = request.GET['author']
        publisher = request.GET['publisher']
        publishdate = request.GET['publishdate']
        price = float(request.GET['price'])
        authorinfo=search_authorid_by_name('"'+author+'"')
        if authorinfo:
            k=write_book((isbn,title,authorinfo[0],publisher,publishdate,price))
            if k:
                return HttpResponseRedirect('/')
            else:
                return render(request, 'error.html')
        else:
            return HttpResponseRedirect('/lackauthor')
    except:
        return render(request, 'error.html')

def showbook(request):
    bookinfo = read_book()
    books=[]
    for row in bookinfo:
        node1=row[1]
        node2=search_author_by_id(str(row[2]))[1]
        node3=row[5]
        newnode=node1,node2,node3
        books.append(newnode)
    return render_to_response('indexdemo.html',{'books':books})
def showauthor(request):
    authorinfo = read_author()
    authors=[]
    for row in authorinfo:
        node1=row[1]
        node2=row[2]
        node3=row[3]
        newnode=node1,node2,node3
        authors.append(newnode)
    return render_to_response('showauthor.html',{'authors':authors})

def delbook(request,n):
    index = int(n)-1
    info=read_book()
    num=info[index][0]
    print num
    print n
    r=delete_book('"'+num+'"')
    return HttpResponseRedirect('/')

def delauthor(request):
    index = int(request.GET['num'])-1
    info=read_author()
    num=info[index][0]
    print num
    r=delete_author(int(num))
    return HttpResponseRedirect('/showauthor')

def showerror(request):
    return render(request, 'lackauthor.html')

def updatebookpre(request,n):
    num=n
    bookinfo =read_book()[int(num)-1]
    isbn=bookinfo[0]
    title=bookinfo[1]
    author= search_author_by_id(int(bookinfo[2]))[1]
    publisher=bookinfo[3]
    publishdate=bookinfo[4]
    price=float(bookinfo[5])
    return render_to_response('upbook.html',{'a':isbn,'b':title,'c':author,'d':publisher,'e':publishdate,'f':price,'num':num})
def updatebook(request):
    try:
        num=int(request.GET['num'])
        isbn = request.GET['isbn']
        title = request.GET ['title']
        author = request.GET['author']
        publisher = request.GET['publisher']
        publishdate = request.GET['publishdate']
        price = float(request.GET['price'])
        authorinfo=search_authorid_by_name('"'+author+'"')
        if authorinfo:
            info=read_book()[num-1]
            delete_book(info[0])
            k=write_book((isbn,title,authorinfo[0],publisher,publishdate,price))
            if k:
                return HttpResponseRedirect('/')
            else:
                return render(request, 'error.html')
        else:
            return HttpResponseRedirect('/lackauthor')
    except:
        return render(request, 'error.html')

def searchauthor(request):
    name=request.GET['authorname']
    info=search_authorid_by_name('"'+name+'"')
    if info:
        id=info[0]
        bookinfo = search_book_by_authorid(id)
        books=[]
        for row in bookinfo:
            node1=row[1]
            node2=search_author_by_id(str(row[2]))[1]
            node3=row[5]
            newnode=node1,node2,node3
            books.append(newnode)
        return render_to_response('search.html',{'books':books})
    else:
        return render(request, 'lackauthor1.html')

def showbookinfo(request,n):
    num=n
    bookinfo =read_book()[int(num)-1]
    isbn=bookinfo[0]
    title=bookinfo[1]
    author= search_author_by_id(int(bookinfo[2]))[1]
    publisher=bookinfo[3]
    publishdate=bookinfo[4]
    price=float(bookinfo[5])
    return render_to_response('bookdetail.html',{'isbn':isbn,'title':title,'author':author,'publisher':publisher,'publishdate':publishdate,'price':price,'num':num})

def showauthorinfobybook(request,n):
    num=n
    book=read_book()[int(num)-1]
    authorinfo=search_author_by_id(int(book[2]))
    authorname=authorinfo[1]
    age=authorinfo[2]
    country=authorinfo[3]
    bookinfo=search_book_by_authorid(int(book[2]))
    books=[]
    for row in bookinfo:
        books.append(row[1])
    return render_to_response('authordetail.html',{'name':authorname,'age':age,'country':country,'books':books})

def showauthorinfobyself(request,n):
    num=n
    authorinfo=read_author()[int(num)-1]
    authorname=authorinfo[1]
    age=authorinfo[2]
    country=authorinfo[3]
    bookinfo=search_book_by_authorid(authorinfo[0])
    books=[]
    for row in bookinfo:
        books.append(row[1])
    return render_to_response('authordetail.html',{'name':authorname,'age':age,'country':country,'books':books})

def initial(request):
    a=initialize()
    b=insertdata()
    return HttpResponse((a,b))
