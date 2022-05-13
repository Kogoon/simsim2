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

        #lunch_list = ["마라탕", "맥도날드", "인도카레", "육수당", "돈카츠", "서브웨이", "라멘", "초밥"]
        #menu = "".join(random.sample(lunch_list, k=1))

        all_menus = Menus.objects.all()

        try:
            cursor = connection.cursor()

            randomsql = "select content from menuapp_menus order by rand() limit 1"
            
            result = cursor.execute(randomsql)
            menuss = cursor.fetchall()

            connection.commit()
            connection.close()

            return render(request, 'menuapp/menu.html',
            {
                'menu': menuss[0][0],
                'menu_lists': all_menus,
            })
 
        except:
            print("except")
            return render(request, 'menuapp/menu.html', 
            {
                'menu': '등록된 메뉴가 없습니다.',
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