django-piehunter
================

Automatic Tastypie URL builder by way of import discovery.



In your toplevel urls.py :

{{{
    from django.conf.urls import patterns, include

    from piehunter import PieHunter

    api_urls = PieHunter(api_name='v1',
                         dotted_path='api.resources',
                         enabled_attribute='EnabledResources')

    urlpatterns = patterns('',
                           surl(r'^api/',          include(api_urls)),
                           surl(r'^beta/',         include('hunger.urls')),
                           )
}}}

Now in your applications you would have a directory structure like so :

{{{
/
    __init__.py
    urls.py
    models.py
    admin.py
    templates/
    static/
    ...

}}}

Throw your Tastypie resources into the api module to end up with something like :

{{{
/
    __init__.py
    urls.py
    models.py
    admin.py
    templates/
    static/
    api/
        resources.py
        ...
    ...
}}}

At the end of your `api.resources` module, include a list/set of resources you want to use :

{{{
EnabledResources = (TrooperResource,
                    DeathstarResource,
                    EvilGrinResource,
                    )
}}}

That's it, piehunter will now hunt for and include any resource found to be in a api.resources.EnabledResources