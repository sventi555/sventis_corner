from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


# Create your views here.

def list_graphics(request):
    graphic_list = models.Graphic.objects.all()
    paginator = Paginator(graphic_list, 8)
    page = request.GET.get('page')
    graphics = paginator.get_page(page)
    return render(request, 'graphics/list_graphics.html', {
        'graphics': graphics,
    })


def graphic_detail(request, pk):
    graphic = models.Graphic.objects.get(pk=pk)
    js_files = graphic.file_set.filter(type__name='js')
    other_files = graphic.file_set.exclude(type__name='js')
    return render(request, 'graphics/graphic_detail.html', {
        'graphic': graphic,
        'js_files': js_files,
        'other_files': other_files,
    })