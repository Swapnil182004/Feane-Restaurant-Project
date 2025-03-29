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
    review = Feedback.objects.all()
    return render(request, 'feedback.html', {'review' : review})

def SubmitFeedback(request):
    if request.method == 'POST':
        name = request.POST.get('user_name', '').strip()
        feedback_description = request.POST.get('feedback_desc', '').strip()
        rating = request.POST.get('rating', '').strip()
        photo = request.FILES.get('user_photo')  # Use request.FILES for images

        # Check for empty values
        if not name or not feedback_description or not rating:
            return redirect('home')

        try:
            rating = int(rating)  # Ensure rating is a valid integer
        except ValueError:
            return redirect('home')

        # Save feedback to database
        review_data = Feedback(
            User_Name=name,
            Feedback_Description=feedback_description,
            Rating=rating,
            User_Image=photo
        )
        # If the user uploaded an image, save it
        if photo:
            review_data.User_Image = photo

        return redirect('home')  # Redirect after submission

    return render(request, 'feedback.html')  # If method is not POST, redirect to home page
