from django.http import HttpResponse


from django.shortcuts import render

def firstTemplate(request):

    #dict1={'name':"Modi",'country':'India'}

    return render(request,'index.html')


def firstDef(request):
    return HttpResponse("Hellow World")

def otherfunction(request):

    djangotext=print(request.GET.get('textfromhome'))
    print(djangotext)

    return HttpResponse('''Random method called<br>
            <a href="/">Back to home</a>''')


def whysostupid(request):
    return HttpResponse("Why so Stupid Returned")