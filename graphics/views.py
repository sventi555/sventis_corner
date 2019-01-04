from django.shortcuts import render
from graphics import models


def list_graphics(request):
    return render(request, 'graphics/list_graphics.html',
                  {
                      'graphics': models.Graphic.objects.all()
                  })


def graphic_detail(request, title):
    graphic = models.Graphic.objects.get(title=title)
    return render(request, 'graphics/graphic_detail.html',
                  {
                      'graphic': graphic,
                  })
