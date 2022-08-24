import logging
from django.http import HttpResponse
from django.views.generic import TemplateView

_logger = logging.getLogger(__name__)


# def maintenance(request):
#     _logger.warning(request)
#     return HttpResponse("Thi site is under maintenance")
#

class Maintenance(TemplateView):
    template_name = 'maintenance.html'

class NotFound(TemplateView):
    template_name = "404.html"

class HomePage(TemplateView):
    template_name = "home.html"
