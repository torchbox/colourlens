import urllib
from django.db.models import Avg, Sum, Count
from django import forms
from django.forms.widgets import Input
from django.shortcuts import render
from colourlens.models import Artwork, Colour

PROM_ATTRS = {'min': '0', 'max': '100', 'step': '5'}
DIST_ATTRS = {'min': '0', 'max': '50', 'step': '1'}


class RangeInput(Input):
    input_type = "range"


class ColourForm(forms.Form):

    def __init__(self, *args, **kwargs):
        """
        Add classes to denote type of input
        """
        super(ColourForm, self).__init__(*args, **kwargs)

        for k, v in self.fields.iteritems():
            if v.widget.__class__ == forms.CheckboxInput:
                v.widget.attrs['class'] = 'colourbox'
            elif v.widget.__class__ == RangeInput:
                v.widget.attrs['class'] = 'slider'

    black = forms.BooleanField(required=False)
    grey = forms.BooleanField(required=False)
    silver = forms.BooleanField(required=False)
    white = forms.BooleanField(required=False)
    red = forms.BooleanField(required=False)
    maroon = forms.BooleanField(required=False)
    brown = forms.BooleanField(required=False)
    orange = forms.BooleanField(required=False)
    yellow = forms.BooleanField(required=False)
    lime = forms.BooleanField(required=False)
    green = forms.BooleanField(required=False)
    olive = forms.BooleanField(required=False)
    cyan = forms.BooleanField(required=False)
    teal = forms.BooleanField(required=False)
    blue = forms.BooleanField(required=False)
    navy = forms.BooleanField(required=False)
    magenta = forms.BooleanField(required=False)
    purple = forms.BooleanField(required=False)
    prominence = forms.IntegerField(label="Increase colour area",
                                    widget=RangeInput(attrs=PROM_ATTRS))
    distance = forms.IntegerField(label="Broaden palette",
                                  widget=RangeInput(attrs=DIST_ATTRS))
    submitted = forms.CharField(widget=forms.HiddenInput())


class ColourChoice(object):
    def __init__(self, selected_colours, colour):
        self.selected_colours = selected_colours
        self.colour = colour

    @property
    def artwork_count(self):
        return self.colour.artwork__count

    @property
    def hex_value(self):
        return self.colour.hex_value

    @property
    def query_string(self):
        # Get new set of selected colours
        if self.colour.hex_value in self.selected_colours:
            new_selected_colours = self.selected_colours.difference(set([self.colour.hex_value]))
        else:
            new_selected_colours = self.selected_colours.union(set([self.colour.hex_value]))

        if new_selected_colours:
            return urllib.urlencode([
                ('colour', colour)
                for colour in new_selected_colours
            ])


def index(request, institution=False):
    """
    Search and browse colours
    """
    DISTANCE = 20
    artworks = Artwork.objects.select_related().all()
    colours = Colour.objects.all()
    req_colours = request.GET.getlist('colour', [])
    startyear = request.GET.get('startyear', None)
    endyear = request.GET.get('endyear', None)

    colour_filters = {}

    if startyear:
        artworks = artworks.filter(year__gte=startyear)
        colour_filters['artwork__year__gte'] = startyear

    if endyear:
        artworks = artworks.filter(year__lte=endyear)
        colour_filters['artwork__year__lte'] = endyear

    for hex_value in req_colours:
        artworks = artworks.filter(
            colours__hex_value=hex_value,
            colourdistance__distance__lte=DISTANCE,
        )

    if institution:
        artworks = artworks.filter(institution=institution)
        colour_filters['artwork__institution'] = institution

    artworks = artworks.annotate(
        ave_distance=Avg('colourdistance__distance'),
        ave_presence=Avg('colourdistance__presence'),
        tot_presence=Sum('colourdistance__presence'),
        tot_prominence=Sum('colourdistance__prominence'),
        ave_prominence=Avg('colourdistance__prominence'),
    )

    artworks = artworks.order_by('-tot_presence').distinct()
    artworks_count = artworks.count()

    if req_colours:
        colour_filters['artwork__id__in'] = [a.id for a in artworks[:990]]
        colour_filters['colourdistance__distance__lte'] = DISTANCE

    colours = colours.filter(**colour_filters)
    colours = colours.annotate(Count('artwork', distinct=True)).order_by('hue')
    colour_count = colours.count()

    colour_width = 99.4 / colour_count

    if colour_count > 0:
        total_palette = sum(c.artwork__count for c in colours)
    else: 
        total_palette = 0

    institutions = Artwork.objects.all().values('institution').distinct()

    return render(request, 'colour.html', {
        'artworks': artworks[:40],
        'colours': [ColourChoice(set(req_colours), colour) for colour in colours],
        'colour_count': colour_count,
        'colour_width': colour_width,
        'total_palette': total_palette,
        'found': artworks_count,
        'institution': institution,
        'institutions': institutions,
        'req_colours': req_colours,
    })
