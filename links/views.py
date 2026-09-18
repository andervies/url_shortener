import json
import random
import string

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Link
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
def generate_code():
    characters = string.ascii_letters + string.digits
    print(characters)

    return "".join(
        random.choices(characters, k=6)
    )

@csrf_exempt
def create_link(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    print(request.body)

    body = json.loads(request.body)
    url = body["url"]
    print(url)

    link = Link.objects.create(url=url, code=generate_code())

    return JsonResponse({"id": link.id, "url": link.url, "code": link.code, "clicks": link.clicks}, status=201)

def redirect_link(request, code):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed."}, status="405")

    
    found = get_object_or_404(Link, code=code)
    found.clicks += 1

    found.save()
    return redirect(found.url)
