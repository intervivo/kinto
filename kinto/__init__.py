import pkg_resources
import logging

from pyramid.config import Configurator
from cliquet import initialize_cliquet
from cliquet.authorization import RouteFactory

# Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version

# Main kinto logger
logger = logging.getLogger(__name__)


def main(global_config, **settings):
    config = Configurator(settings=settings, root_factory=RouteFactory)
    initialize_cliquet(config, version=__version__)
    config.scan("kinto.views")
    return config.make_wsgi_app()
