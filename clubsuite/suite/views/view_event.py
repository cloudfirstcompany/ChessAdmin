from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import View

from suite.models import Event as EventModel
from suite.models import Club
from . import models

class Event(LoginRequiredMixin, View):
    template_name = 'event.html'
    def get(self, request, club_id, event_id, *args, **kwargs):
       #
       club = get_object_or_404(Club, pk=club_id)
       event = EventModel.objects.get(pk=event_id)
       mems = club.members.all()

       members = []
       for mem in mems:
         member = {'user': mem, 'group': None } # TODO group
         print(member)
         members.append(member)

       print(members)

       return render(request, self.template_name, {'club': club, 'members' : members, 'event': event})
