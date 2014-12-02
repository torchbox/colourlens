from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Sum, Count

from colourlens.models import Artwork, Colour


def index(request):
    colours = Colour.objects.all().order_by('hue')

    try:
        colour_width = 99.4 /  colours.count()
    except ZeroDivisionError:
        colour_width = 0

    return render(request, 'index.html', {
        'colours': colours,
        'colour_width': colour_width,
        'colours_count': colours.count()
    })


def artwork_list(request):
    requested_colours = Colour.objects.filter(
        hex_value__in=map(lambda x: '#' + x, request.GET.getlist('colour', []))
    )

    artworks = Artwork.objects.select_related().filter(
        colours__in=requested_colours,
        colourdistance__distance__lte=20,
    )

    artworks = artworks.annotate(
        ave_distance=Avg('colourdistance__distance'),
        ave_presence=Avg('colourdistance__presence'),
        tot_presence=Sum('colourdistance__presence'),
        tot_prominence=Sum('colourdistance__prominence'),
        ave_prominence=Avg('colourdistance__prominence'),
    )

    artworks = artworks[:10]

    colours = Colour.objects.all()
    colours = colours.annotate(Count('artwork', distinct=True)).order_by('hue')
    colour_width = 99.4 /  colours.count()

    return render(request, 'ajax/artwork_list.html', {
        'requested_colours': requested_colours,
        'artworks': artworks,
        'colours': colours,
        'colour_width': colour_width,
    })


def artwork_info(request, accession_number):
    artwork = get_object_or_404(Artwork, accession_number=accession_number)

    return render(request, 'ajax/artwork_info.html', {
        'artwork': artwork,
    })
