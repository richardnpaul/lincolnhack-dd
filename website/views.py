from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mps.models import MP
from userprofile.models import UserProfile
from voting.models import Bill, Votes


@login_required
def users_profile(request):
    user_profile = UserProfile.objects.get(user=request.user.id)
    user_mp = MP.objects.get(id=user_profile.mp.id)
    return render(request, 'user_profile.html', {'user': user_profile,
                                            'mp': user_mp })


@login_required
def mp_profile(request, mp_id):
    user_profile = UserProfile.objects.get(user=request.user.id)
    mp = MP.objects.get(id=mp_id)
    return render(request, 'mp_profile.html', {'mp': mp, 'user': request.user,
                                               'user_profile': user_profile})


@login_required
def bills(request):
    user_profile = UserProfile.objects.get(user=request.user.id)
    user_mp = MP.objects.get(id=user_profile.mp.id)
    voted = []
    bills = Bill.objects.all()
    for bill in bills:
        if Votes.objects.all().filter(bill=bill).filter(voter=request.user):
            voted.append(bill)
    return render(request, 'user_bills.html', {'user': request.user,
                                               'mp': user_mp,
                                               'user_profile': user_profile,
                                               'voted': voted,
                                               })


@login_required
def vote(request):

    return render(request, 'user_vote.html', {})