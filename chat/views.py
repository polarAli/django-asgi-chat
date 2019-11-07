from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Group, Message


@login_required
def index(request):
    context = {
        'groups': request.user.chats.all()
    }
    return render(request, 'chat/index.html', context)


@login_required
def chat(request, room_name):
    chat = get_object_or_404(Group, name=room_name)
    context = {
        'chat_messages': chat.messages.all(),
        'room_name': chat.name
    }
    return render(request, 'chat/room.html', context)
