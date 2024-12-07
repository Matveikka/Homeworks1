from django.shortcuts import render


# Create your views here.
def game_platform(request):
    return render(request, "fourth_task/platform.html")


def game(request):
    games = {'games': ['Atomic Heart', "Cyberpunk 2077"]}
    return render(request, "fourth_task/games.html", context=games)


def cart(request):
    return render(request, "fourth_task/cart.html")
