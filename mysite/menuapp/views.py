from django.shortcuts import render

import random

# Create your views here.

def index(request):

    if request.method == "GET":
            
        '''homepage site'''
        lunch_list = ["마라탕", "맥도날드", "인도카레", "육수당", "돈카츠", "서브웨이", "라멘", "초밥"]
        menu = "".join(random.sample(lunch_list, k=1))
        
        print(menu)

        lunch_menu = {'menu': menu,}

        return render(request, 'menuapp/index.html', lunch_menu)