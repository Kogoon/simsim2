from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Menus
from django.db import connection

import random

# Create your views here.

def get_menu(request):

    if request.method == "GET":
        '''homepage site'''

        lunch_list = ["마라탕", "맥도날드", "인도카레", "육수당", "돈카츠", "서브웨이", "라멘", "초밥"]
        menu = "".join(random.sample(lunch_list, k=1))

        all_menus = Menus.objects.all()
        cursor = connection.cursor()

        randomsql = "select content from menuapp_menus order by rand() limit 1"
        result = cursor.execute(randomsql)
        books = cursor.fetchall()

        connection.commit()
        connection.close()

        print(books[0][0])



        #lunch_list.append(all_menus.content)

        return render(request, 'menuapp/menu.html', 
        {
            'menu': books[0][0],
            'menu_lists': all_menus,
        })


    elif request.mothod == "POST":
        pass


""""
def menuappView(request):

    all_menus = Menus.objects.all()
    return render(request, 'menulist.html', 
    {'menu_lists': all_menus})
"""

def addMenu(request):
    x = request.POST['content']
    new_menu = Menus(content = x)
    new_menu.save()
    
    return HttpResponseRedirect(reverse('menuapp:menu'))

def deleteMenu(request, i):
    y = Menus.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect(reverse('menuapp:menu')) 