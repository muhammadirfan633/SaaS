from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message_text = request.POST.get("message", "").strip()

        if name and email and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
            )
            messages.success(request, "Thank you for your message! You will get a reply soon.")
            return redirect("contact")
        else:
            messages.error(request, "Please fill in your name, email, and message.")

    return render(request, "core/contact_us.html")