from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.shortcuts import redirect

from rest_framework import viewsets,renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import Files
from .serializers import FileSerializer
from .forms import UserForm
# Create your views here.


def addUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return HttpResponse("done")
    else:
        form = UserForm()

    return render(request, 'sync/signup.html', {'form':form})

class UserProfileView(DetailView):
    model = User
    slug_field = "username"
    template_name = "sync/file_list_test.html"


class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    slug_field = "owner"
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    template_name = 'sync/file_list.html'
    http_method_names = ['get', 'post', 'head', 'delete']

    def get_queryset(self):
        return Files.objects.filter(owner = self.request.user)

    @list_route(renderer_classes=[renderers.TemplateHTMLRenderer])
    def upload(self, request, *args, **kwargs):
        serializer = FileSerializer()
        return render(request, 'sync/upload.html', {'serializer': serializer})
