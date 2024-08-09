def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'src.settings.config.debug_toolbar.show_toolbar',
    # Rest of config
}

INTERNAL_IPS = ['127.0.0.1', ]
