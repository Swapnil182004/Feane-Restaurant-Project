from django.shortcuts import render, redirect
from django.http import HttpResponse
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items  # Importing models
from django.contrib import messages

# Create your views here.

def HomeView(request):
    items = Items.objects.all()
    item_list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html', { 'items': items, 'item_list': item_list, 'review': review })

def AboutView(request):
    return render(request, 'about.html')

def MenuView(request):
    items = Items.objects.all()
    item_list = ItemList.objects.all()
    return render(request, 'menu.html', { 'items': items, 'item_list': item_list })

def TableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')    # Getting data from form
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        cab_required = request.POST.get('cab_required') == 'on'  # Checkbox returns 'on' when checked
        pickup_location = request.POST.get('pickup_location') if cab_required else None

        if name and email and len(phone_number) == 10 and total_person and booking_date:
            data = BookTable(
                Name=name,
                Phone_Number=phone_number,
                Email=email,
                Total_Person=total_person,
                Booking_Date=booking_date,
                Booking_Time=booking_time,
                Cab_Required=cab_required,
                Pickup_Location=pickup_location
            )
            data.save()
            messages.success(request, "Your table has been booked successfully!")

    return render(request, 'book_table.html')

def FeedbackView(request):
    review = Feedback.objects.all().order_by('-id')  # Show latest first
    return render(request, 'feedback.html', {'review' : review})


def SubmitFeedback(request):
    if request.method == 'POST':
        name = request.POST.get('user_name', '').strip()
        feedback_description = request.POST.get('feedback_desc', '').strip()
        rating = request.POST.get('rating', '').strip()
        photo = request.FILES.get('user_photo')

        if not name or not feedback_description or not rating:
            messages.error(request, "Please fill out all required fields.")
            return redirect('feedback')

        try:
            rating = int(rating)
        except ValueError:
            messages.error(request, "Invalid rating value.")
            return redirect('feedback')

        review_data = Feedback(
            User_Name=name,
            Feedback_Description=feedback_description,
            Rating=rating,
            User_Image=photo if photo else None
        )
        review_data.save()

        messages.success(request, "Thank you for your review!")
        return redirect('feedback')

    return redirect('feedback')  # If GET request, redirect to feedback page
