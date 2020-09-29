from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_safe
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


@require_safe
def index(request):
    return render(request, 'index.html')


@require_safe
def tos(request):
    return render(request, 'tos.html')


class LanguageView(APIView):

    @action(['GET'], url_path='', url_name="languages")
    def get(self, request, *args, **kwargs):
        return Response([{l[0], l[1]} for l in settings.LANGUAGES], content_type="application/json")
