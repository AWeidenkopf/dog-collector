class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lolo', 'German Shepherd', 'Kinda rude.', 3),
  Dog('Sachi', 'Poodle', 'Nice big puppy.', 0),
  Dog('Fancy', 'Chihuahua', 'Angry fluff ball.', 4),
  Dog('Bonk', 'Labrador', 'Your best friend.', 6)
]

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello ૮ ^ ﻌ ^ ა</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })