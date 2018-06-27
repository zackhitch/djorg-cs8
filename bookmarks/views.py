from django.shortcuts import render
from .models import Bookmark, PersonalBookmark
# Create your views here.


def index(request):
    context = {'bookmarks': Bookmark.objects.all(
    ), 'personal_bookmarks': PersonalBookmark.objects.filter(user=request.user)}
    return render(request, 'bookmarks/index.html', context)
