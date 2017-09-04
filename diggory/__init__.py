"""Main entry point
"""
import pkg_resources
from pyramid.config import Configurator
from kinto.core import initialize


# Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version


DEFAULT_SETTINGS = {
    'project_name': 'diggory',
    'project_docs': 'https://diggory.readthedocs.io/',
    'multiauth.policies': '',
}


def main(global_config, **settings):
    config = Configurator(settings=settings)
    initialize(config, __version__, "diggory", default_settings=DEFAULT_SETTINGS)
    config.scan("diggory.views")
    return config.make_wsgi_app()
