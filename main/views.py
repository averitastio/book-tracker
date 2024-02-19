from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Nazwa Allysa',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
