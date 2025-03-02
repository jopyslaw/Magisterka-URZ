from django.shortcuts import render

# Create your views here.
def comment_view_unsecured(request):
    comment = request.GET.get("comment", "")
    return render(request, "comment-unsecured.html", {"comment": comment})

def comment_view_secured(request):
    comment = request.GET.get("comment", "")
    return render(request, "comment-secured.html", {"comment": comment})