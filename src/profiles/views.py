from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def profile_list_view(request, *args, **kwargs):
    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    return render(request, "profiles/list.html", context)

@login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user
    # profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    if is_me:
        if user.has_perm("visits.view_pagevisit"):
            pass
    return HttpResponse(f"Hello there {username} - {profile_user_obj.id} -{user.id}")


@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    user = request.user
    # user_groups = user.groups.all()
    # if user_groups.filter(name__icontains='basic').exists():
    #     return HttpResponse("Congrats")
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {
        "object": User.objects.filter(is_active=True),
        "instance": profile_user_obj,
        "is_me": is_me
    }
    return render(request, "profiles/detail.html", context)