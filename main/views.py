from django.shortcuts import render

def show_main(request):
    context = {
        'appname': 'PakBepeStore',
        'name': 'Sheryl',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
