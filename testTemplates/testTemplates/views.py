#from django.http import HttpResponse
from django.shortcuts import render


MENU = {"главная":"/", "каталог":"/catalog", "о сайте":"/about"}

def main_page(request):

    title = "Главная страница"
    data = {"menu": MENU, "title": title}
    return render(request, "./index.html", context=data)

def about_page(request):

    title = "О компании"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)


    #text_html = "<h2> Main page</h2>"
    #just_text = "Hello"
    #return HttpResponse(text)
  #  return render(request, "./index.html", context=data)
   # data = {}
  #  {
    #    "string1" : text_html,
   #     "string2" : just_text,
  #      "string3" : "static text",

   # })
