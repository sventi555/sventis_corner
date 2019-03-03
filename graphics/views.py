from django.core.paginator import Paginator
from django.shortcuts import render
from graphics import models


def list_graphics(request):
    graphics_list = models.Graphic.objects.all()
    paginator = Paginator(graphics_list, 10)
    page = request.GET.get('page')
    graphics = paginator.get_page(page)
    return render(request, 'graphics/list_graphics.html',
                  {
                      'graphics': graphics
                  })


def graphic_detail(request, title):
    graphic = models.Graphic.objects.get(title=title)
    return render(request, 'graphics/graphic_detail.html',
                  {
                      'graphic': graphic,
                  })
