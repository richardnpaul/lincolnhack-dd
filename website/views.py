from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from mps.models import MP
from userprofile.models import UserProfile
from voting.models import Bill


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
    bills = Bill.objects.prefetch_related('votes','votes__voter').all()
    user_voted = bills.filter(votes__voter__id=request.user.id).all()
    user_not_voted = bills.exclude(votes__voter__id=request.user.id).all()
    return render(request, 'user_bills.html', {'user': request.user,
                                               'mp': user_mp,
                                               'voted_bills': user_voted,
                                               'unvoted_bills': user_not_voted})
