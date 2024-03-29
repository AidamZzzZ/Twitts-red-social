from django.shortcuts import render, redirect
from .models import Profile
from .forms import TwittsForm

def dashboard(request):
    form = TwittsForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            twitt = form.save(commit=False)
            twitt.user = request.user
            twitt.save()
            return redirect("twitts:home")
    return render(request, 'twitts/dashboard.html', {'form':form})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'twitts/profile_list.html', {'profiles':profiles})
    
def detail_profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method=="POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action =="unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, 'twitts/profile_detail.html', {'profile':profile})