
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import (
    SiteSettings,
    Service,
    Destination,
    Experience,
    Testimonial,
    SuccessStory,
    Enquiry,
)


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        destination = request.POST.get("destination", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(
                request,
                "Please provide your name, email, and message."
            )
        else:
            Enquiry.objects.create(
                name=name,
                email=email,
                phone=phone,
                interested_destination=destination,
                message=message,
            )
            messages.success(
                request,
                "Thank you! Your enquiry has been submitted successfully."
            )

        return redirect("home")

    context = {
        "site": SiteSettings.objects.order_by("-updated_at").first(),
        "services": Service.objects.filter(is_active=True),
        "destinations": Destination.objects.filter(is_active=True),
        "experiences": Experience.objects.all(),
        "testimonials": Testimonial.objects.filter(is_active=True),
        "success_stories": SuccessStory.objects.filter(is_active=True),
    }

    return render(request, "index.html", context)
