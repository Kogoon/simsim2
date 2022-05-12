from django.shortcuts import render

import random 

def lotto():

    lotto_nums = random.sample(range(1, 46), 6)

    return lotto_nums

# Create your views here.
def get_lotto_nums(request):
    if request.method == "GET":

        lotto_nums = lotto()
        
        data = {
            'lotto_nums': lotto_nums,
        }

        return render(request, 'lottoapp/lotto.html', data)