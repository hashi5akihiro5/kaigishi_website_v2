from .base import *

try:
    from .local import *
except:
    pass


if not DEBUG:
    import django_heroku
    import dj_database_url

    django_heroku.settigs(locals())

    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)