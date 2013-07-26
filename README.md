django-piehunter
================

Automatic Tastypie URL builder by way of import discovery through all your `INSTALLED_APPS`.

Nothing complex, just a piece of functionality I found I was repeating over and over in the 
projects I've been deploying recently.



In your toplevel urls.py :

```
    from django.conf.urls import patterns, include
    from piehunter import PieHunter
    api_urls = PieHunter(api_name='v1',
                         dotted_path='api.resources',
                         enabled_attribute='EnabledResources')
    urlpatterns = patterns('',
                           surl(r'^api/',          include(api_urls)),
                           surl(r'^beta/',         include('hunger.urls')),
                           )
```

Now in your applications you would have a directory structure like so :

```
/
    __init__.py
    urls.py
    models.py
    admin.py
    templates/
    static/
    ...
```

Throw your Tastypie resources into the api module to end up with something like :

```
/
    __init__.py
    urls.py
    models.py
    admin.py
    templates/
    static/
    api/
        __init__.py
        resources.py
        ...
    ...
```

At the end of your `api.resources` module, include a list/set of resources you want piehunter to find :

```
from tastypie.resources import ModelResource

class TrooperResource(ModelResource):
   ...

class DeathstarResource(ModelResource):
   ...

class EvilGrinResource(ModelResource):
   ...

EnabledResources = (TrooperResource,
                    DeathstarResource,
                    EvilGrinResource,
                    )
```

That's it, piehunter will now hunt through all the applications in your `INSTALLED_APPS` 
and include any resource found to be in an applications `api.resources.EnabledResources`.
 
