from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from tracker.models import Food, Consumed


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        user = authenticate(username='test', password='test')
        if user is not None:
            login(request, user)
        return redirect('/')
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(id=food_consumed)
        user = request.user
        consumed = Consumed(user=user, food=consume)
        consumed.save()
        food = Food.objects.all()
    else:
        food = Food.objects.all()
    consumed_food = Consumed.objects.filter(user=request.user)
    return render(request, 'tracker/index.html', {'food': food, 'consumed_food': consumed_food})


def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('/admin')
    consumed = Consumed.objects.get(id=id)
    if request.method == 'POST':
        consumed.delete()
        return redirect('/')
    return render(request, 'tracker/delete.html')
