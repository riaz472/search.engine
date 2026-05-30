"""PythonAnywhere WSGI entry-point.

Usage in PythonAnywhere WSGI config file:
    import sys, os
    sys.path.insert(0, '/path/to/search.engine')
    os.environ.setdefault('SEARXNG_SETTINGS_PATH', '/path/to/search.engine/searx/settings.yml')
    from wsgi import application
"""
from searx.webapp import app as application

__all__ = ["application"]
