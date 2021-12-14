from django.shortcuts import render

# Create your views here.

attractions_list = [
    {'attraction_name': "Niagara Falls", "state": "New York"},
    {'attraction_name': "Grand Canyon National Park", "state": "Arizona"},
    {'attraction_name': "Mall of America", "state": "Minnesota"},
    {'attraction_name': "Mount Rushmore", "state": "South Dakota"},
    {'attraction_name': "Times Square", "state": "New York"},
    {'attraction_name': "Walt Disney World", "state": "Florida"},
    {'attraction_name': "Test Attraction", "state": "Quebec"},
]


def home(request):
    context = {"attractions": attractions_list}
    return render(request, 'tourist_attractions/home.html', context)


def details(request, statename):
    context = {"attractions": attractions_list, "statename": statename.replace("-", " ")}
    return render(request, 'tourist_attractions/details.html', context)

