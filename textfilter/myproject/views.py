from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get('text', 'default')

    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        dix = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        dix = {'purpose':'Changed to Upprcase','analyzed_text':analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        dix = {'purpose':'Remove New Lines', 'analyzed_text':analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        dix = {'purpose':'Remove Extra Space', 'analyzed_text':analyzed}
        djtext = analyzed
        
    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("""<html><h2  style="color: red; font-family: sans-serif;">Please select the operation from one of them...</h2></html>""")
    return render(request, 'analyze.html', dix)
        
