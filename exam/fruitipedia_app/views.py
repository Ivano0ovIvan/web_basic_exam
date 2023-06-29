from django.shortcuts import render, redirect

from exam.fruitipedia_app.forms import DeleteFruitForm, EditFruitForm, ProfileCreateModelForm, FruitCreateModelForm, \
    ProfileEditModelForm
from exam.fruitipedia_app.models import FruitModel, ProfileModel


def index(request):
    return render(request, 'common/index.html')

def dashboard(request):
    fruits = FruitModel.objects.all()
    context = {'fruits': fruits}

    return render(request, 'common/dashboard.html', context)



def create_fruit(request):
    form = FruitCreateModelForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('dashboard')

    context = {'form': form}

    return render(request, 'fruits/create-fruit.html', context)

def fruit_details(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    context = {'fruit': fruit}

    return render(request, 'fruits/details-fruit.html', context)

def fruit_edit(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    form = EditFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()

        return redirect('dashboard')

    context = {'form': form, 'fruit':fruit}

    return render(request, 'fruits/edit-fruit.html', context)

def fruit_delete(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    form = DeleteFruitForm(request.POST or None, instance=fruit)
    for field in form.fields:
        form.fields[field].required = False
    if form.is_valid():
        form.save()

        return redirect('dashboard')

    context = {'form': form, 'fruit': fruit}

    return render(request, 'fruits/delete-fruit.html', context)

def profile_create(request):
    form = ProfileCreateModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}

    return render(request, 'profile/create-profile.html', context)

def profile_details(request):
    profile = ProfileModel.objects.all().first()
    fruit = FruitModel.objects.count()
    context = {'profile': profile, 'fruit':fruit}

    return render(request, 'profile/details-profile.html', context)
def profile_edit(request):
    profile = ProfileModel.objects.all().first()
    form = ProfileEditModelForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile_details')

    context = {'form':form, 'profile':profile}

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = ProfileModel.objects.all().first()
    fruits = FruitModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        fruits.delete()

        return redirect('index')

    return render(request, 'profile/delete-profile.html')