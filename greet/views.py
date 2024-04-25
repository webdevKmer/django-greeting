from django.shortcuts import render
import random
from .models import Person
# Create your views here.

names = [
    'Iori', 'Adrien', 'Patrick', 'Lionel', 'Vanessa', 'Charlotte', 'Nathan', 'Maxime'
]

people = Person.objects.all()


def home(request):
    return render(request, 'greet/home.html')

def greet_person(request):
    index = random.randint(0,len(people)-1)
    person = people[index]
    age = 2024 - person.birthyear
    return render(request, 'greet/greet_person.html', {'person': person, 'age': age})

def greet(request):
    index = random.randint(0,7)
    name = names[index]
    return render(request, 'greet/greet.html', {'name': name})