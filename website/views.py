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
    bills = Bill.objects.all()
    bills.filter(votes__voter__id=request.user.id).all()#.filter(votes__bill_id=None)
    for bill in bills:
        vote = Votes.objects.filter(bill=bill.id).filter(voter=request.user.id)
        for v in vote:
            if not None:
                bill.votes_set.add(v)
        print(bill.votes_set)
    return render(request, 'user_bills.html', {'user': request.user,
                                               'mp': user_mp,
                                               'bills': bills})

