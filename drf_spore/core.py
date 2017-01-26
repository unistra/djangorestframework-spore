import logging
import re
from django.conf import settings
from django.core.urlresolvers import (RegexURLPattern, RegexURLResolver,
                                      LocaleRegexURLResolver)
from .helpers import SporeMethod


def get_urlconf():

    try:
        return __import__(getattr(settings, 'ROOT_URLCONF'), {}, {}, [''])
    except Exception as urlconf_error:
        logger = logging.getLogger('drf-spore')
        logger.critical(
            "Error occurred while trying to load %s: %s",
            getattr(settings, 'ROOT_URLCONF'),
            str(urlconf_error)
        )


def spore_from_urls(patterns):

    sporify_patterns = []

    for url in patterns:

        if isinstance(url, RegexURLResolver):
            base_regex = url.regex
            includes = spore_from_urls(url.url_patterns)
            for included_url in includes:
                regex = re.compile(
                    base_regex.pattern + included_url.regex.pattern,
                    re.UNICODE
                )
                spore_method = SporeMethod('GET', regex)
                sporify_patterns.append(spore_method)

        elif isinstance(url, RegexURLPattern):
            if url.callback.cls.is_spore_view:
                sporify_patterns.append(url)

    return sporify_patterns
