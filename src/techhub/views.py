from django.http import JsonResponse
from django.shortcuts import render
from visits.models import page_visits
def techhub_view(request):
    title = "TechHub site"
    qs = page_visits.objects.all()
    page_visits.objects.create(path=request.path)
    print(f"Page visited: {request.path}")
    context = {"title": title, "total_visits": qs.count(), "visits": qs}
    html_ = "home/home.html"
    return render(request, html_, context)
