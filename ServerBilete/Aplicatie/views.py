from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect
from Aplicatie.models import User
from Aplicatie.models import Sponsor
from Aplicatie.models import Ticket
from Aplicatie.models import Booking


def homepage(request):
    tickets = Ticket.objects.all()
    if request.method == 'POST' and 'login' in request.POST:
        users = User.objects.all()
        for user in users:
            if (request.POST["email"] == user.email) and (request.POST["password"] == user.password):
                request.session["email"] = user.email
                return render(request, 'homepage.html', {
                    'tickets': tickets,
                    'logged': True
                })
    if request.session.get('email', None):
        return render(request, 'homepage.html',  {
                        'tickets': tickets,
                        'logged': True
                    })
    else:
        return render(request, 'homepage.html', {
            'tickets': tickets,
            'logged': False
        })


def register(request):
    return render(request, 'register.html')


def login(request):
    if request.session.get('email', None):
        del request.session["email"]
    if request.method == 'POST':
        print(request.POST["password"])
        print(request.POST["email"])
        new_user = User(email=request.POST["email"], password=request.POST["password"])
        new_user.save()

    return render(request, 'login.html')


def reserve(request):
    try:
        user = User.objects.get(email=request.session["email"])
    except KeyError as e:
        return redirect('/register/')
    ticket = Ticket.objects.get(name=request.POST["ticket"])
    new_booking = Booking(user=user, ticket=ticket)
    new_booking.save()
    tickets = Ticket.objects.all()
    # if request.session.get('email', None):
    #     return render(request, 'homepage.html',  {
    #                     'tickets': tickets,
    #                     'logged': True
    #                 })
    # else:
    #     return render(request, 'homepage.html', {
    #         'tickets': tickets,
    #         'logged': False
    #     })
    return redirect('/homepage/')
