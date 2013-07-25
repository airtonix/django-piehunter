from tastypie.api import Api

from .discovery import autodiscover


class PieHunter(object):
    urlpatterns = None

    def __init__(self, api_name='v1', dotted_path='api.resources', enabled_attribute='EnabledResources'):
        cage = Api(api_name)
        autodiscover(dotted_path, enabled_attribute, cage)
        self.urlpatterns = cage.urls
