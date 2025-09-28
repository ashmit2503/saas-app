import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title" : my_title
    }
    html_template = "home.html"
    PageVisit.objects.create()
    return render(request,html_template,my_context)

def old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title" : my_title
    }
    html_ = """<!DOCTYPE html>
<html>
<head>
    <h1>This is {page_title}</h1>
</head>
<body>
    
</body>
</html>""".format(**my_context)
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)