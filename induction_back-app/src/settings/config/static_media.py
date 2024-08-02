from .dir import *


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = DIR_PRE_APP.child('static')
MEDIA_ROOT = DIR_PRE_APP.child('media')

# This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder is 
# enabled, e.g.
# if you use the collectstatic or findstatic management command or use the static file serving view.
STATICFILES_DIRS = [BASE_DIR.child('static')]
