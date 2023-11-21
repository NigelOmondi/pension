from django.shortcuts import render, get_object_or_404
from .models import User

def home(request):
    return render(request, 'home.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def search_user(request):
    query = request.GET.get('q')

    if query is not None and query != '':
    # Apply the filter
        users = User.objects.filter(name__icontains=query) | User.objects.filter(pension_number__icontains=query)
    else:
    # Return all users
        users = User.objects.all()
        
    context = {
        'query': query,
        'users': users,
    }

    return render(request, 'search_user.html', context)

def change_status(request, pension_number=None):
    if pension_number:
        # Handle the case where pension_number is provided
        user = get_object_or_404(User, pension_number=pension_number)
        user.is_active = not user.is_active
        user.save()
        return render(request, 'user_detail.html', {'user': user})
    else:
        # Handle the case where pension_number is not provided
        # For example, return an error message or redirect to another page
        return render(request, 'error_page.html', {'error_message': 'No pension number provided'})
