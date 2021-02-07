import os
import urllib
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.models import UserProfile
from cars.forms import CarForm, FilterForm, ReportForm
from cars.models import Car, Report


def extract_filter_values(params):
    brand = params['brand'] if 'brand' in params else ''
    year = params['year'] if 'year' in params else ''
    price = params['max_price'] if 'max_price' in params else ''
    region = params['region'] if 'region' in params else ''
    model = params['models'] if 'models' in params else ''
    return brand, year, price, region, model


def index(req):
    (brand, year, price, region, model) = extract_filter_values(req.GET)

    cars = Car.objects.all()
    if brand:
        cars = [x for x in cars if x.brand == brand]
    if year:
        cars = [x for x in cars if x.year >= int(year)]
    if price:
        cars = [x for x in cars if x.price <= int(price)]
    if region:
        cars = [x for x in cars if x.user.region == region]
    if model:
        cars = [x for x in cars if x.model == model]
    context = {
        'cars': cars,
        'filter_form': FilterForm(initial={'brand': brand, 'year': year, 'max_price': price})
    }
    return render(req, 'index.html', context)


def show_car(req, pk):
    car = Car.objects.get(pk=pk)
    can_delete = req.user == car.user.user
    report_form = ReportForm
    if req.method == 'GET':
        context = {
            'car': car,
            'can_delete': can_delete,
            'report_form': report_form,
        }

        return render(req, 'show_car.html', context)

    else:
        form = report_form(req.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.car = car
            added_by = UserProfile.objects.get(user=req.user)
            report.added_by = added_by
            report.save()

            return redirect('show car', car.id)


@login_required
def create_advertisement(req):
    if req.method == 'GET':
        context = {
            'form': CarForm
        }
        return render(req, 'add_car.html', context)
    else:
        form = CarForm(req.POST, req.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            user = User.objects.get(pk=req.user.pk)
            profile = UserProfile.objects.get(user=user)
            car.user = profile
            car.save()
            return redirect('show car', car.id)
        context = {
            'form': form
        }
        return render(req, 'add_car.html', context)


@login_required
def delete_car(req, pk):
    car = Car.objects.get(pk=pk)
    if not req.user.is_superuser and car.user.user != req.user:
        return redirect('index')
    form = CarForm(instance=car)
    if req.method == "GET":
        context = {
            'form': form,
            'car': car
        }
        return render(req, 'delete_car.html', context)
    else:
        if car:
            car.image.delete()
            car.delete()
        return redirect('index')


@login_required
def edit_car(req, pk, *args, **kwargs):
    car = Car.objects.get(pk=pk)
    if not req.user.is_superuser and car.user.user != req.user:
        return redirect('index')
    form = CarForm(instance=car)

    if req.method == 'GET':
        context = {
            'form': form,
            'car': car
        }
        return render(req, 'edit_car.html', context)
    else:

        form = CarForm(
            req.POST,
            req.FILES,
            instance=car,
        )

        if form.is_valid():
            form.save()
            return redirect('show car', car.pk)
        context = {
            'form': form
        }

        return redirect('edit car', car.pk)


def report_view(req):
    if not req.user.is_superuser:
        return redirect('index')

    context = {
        'reports': Report.objects.all()
    }

    return render(req, 'reports.html', context)


def delete_report(req, pk):
    report = Report(pk=pk)
    if report:
        report.delete()
    return redirect('reports')
