from django.shortcuts import render, redirect

from car_collection.car_collection_app.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm, DeleteProfileForm
from car_collection.car_collection_app.models import Car, Profile
from car_collection.car_collection_app.utils import get_profile

"""
•	http://localhost:8000/ - index page
•	http://localhost:8000/catalogue/ - catalogue page
•	http://localhost:8000/car/create/ - car create page
•	http://localhost:8000/car/<car-id>/details/ - car details page
•	http://localhost:8000/car/<car-id>/edit/ - car edit page
•	http://localhost:8000/car/<car-id>/delete/ - car delete page
•	http://localhost:8000/profile/create - profile create page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page
"""


def index(request):
    profile = get_profile()
    return render(request, 'index.html', context={'profile': profile})


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()

    if profile is None:
        return redirect('create_profile')

    context = {
        'profile': profile,
        'cars': cars,
    }

    return render(request, 'catalogue.html', context=context)


def create_car(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateCarForm()

    context = {
        'profile': profile,
        'create_car_form': form
    }

    return render(request, 'car/car-create.html', context=context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car
    }
    return render(request, 'car/car-details.html', context=context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_details', pk=pk)
    else:
        form = EditCarForm(instance=car)

    context = {
        'car': car,
        'edit_car_form': form,
    }
    return render(request, 'car/car-edit.html', context=context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')
    else:
        form = DeleteCarForm(instance=car)

    context = {
        'delete_car_form': form,
        'car': car
    }
    return render(request, 'car/car-delete.html', context=context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'create_profile_form': form
    }
    return render(request, 'profile/profile-create.html', context=context)


def profile_details(request):
    profile = Profile.objects.last()
    cars = Car.objects.all()
    total_car_cost = sum(car.price for car in cars)
    context = {
        'profile': profile,
        'profile_picture': profile.profile_picture,
        'profile_full_name': f'{profile.first_name} {profile.last_name}',
        'profile_username': profile.username,
        'profile_email': profile.email,
        'profile_age': profile.age,
        'total_car_cost': total_car_cost,
    }
    return render(request, 'profile/profile-details.html', context=context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'edit_profile_form': form
    }

    return render(request, 'profile/profile-edit.html', context=context)


def delete_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.delete()
            cars.delete()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'delete_profile_form': form,
    }

    return render(request, 'profile/profile-delete.html', context=context)

