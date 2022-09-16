from django.views.generic.list import ListView
from pet.models import Pet, Owner


class PetList(ListView):
    model = Pet