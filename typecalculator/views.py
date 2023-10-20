from django.http import HttpResponse
from django.shortcuts import render

from typecalculator.services import calculate_summary


def index(request):
    return HttpResponse(calculate_summary(), content_type="application/json")
