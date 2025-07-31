from django.shortcuts import render

from tracker.models import Food, Consumed


# Create your views here.
def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(id=food_consumed)
        user = request.user
        consumed = Consumed(user=user, food=consume)
        consumed.save()
        food = Food.objects.all()

    else:
        food = Food.objects.all()
    return render(request, 'tracker/index.html', {'food': food})
