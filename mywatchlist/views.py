# Create your views here.
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    countAlreadyWatched = 0
    countNotWatched = 0
    # fitur yang menampilkan pesan
    status = ""

    for alreadyWatched in data_mywatchlist:
        if (alreadyWatched.watched == True):
            countAlreadyWatched += 1
        else:
            countNotWatched += 1

    if (countAlreadyWatched >= countNotWatched):
        status = "Selamat, kamu sudah banyak menonton!"
    else:
        status = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_mywatchlist': data_mywatchlist,
        'nama': 'Risa Lestari',
        'studentId': "2106655274",
        'status': status,
    }
    return render(request, "mywatchlist.html", context)


# Mengembalikan Data dalam Bentuk XML


def mywatchlist_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

# Mengembalikan Data dalam Bentuk JSON


def mywatchlist_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")


# Mengembalikan Data dalam Bentuk XML Berdasarkan id


def mywatchlist_by_id_xml(request, id):
    data_mywatchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

# Mengembalikan Data dalam Bentuk JSON Berdasarkan id


def mywatchlist_by_id_json(request, id):
    data_mywatchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
