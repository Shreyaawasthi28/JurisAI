from django.http import JsonResponse
from .summarize import generate_summary

def summarize_text(request):
    text = request.POST.get("text")
    summary = generate_summary(text)
    return JsonResponse({
        "summary": summary
    })
