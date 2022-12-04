from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

__version__ = "1.0.0"


class PluginApp(PluginConfig):
    name = "email_plugin"
    verbose_name = "email_plugin"

    class PretixPluginMeta:
        name = gettext_lazy("email_plugin")
        author = "Heran"
        description = gettext_lazy("Email plugin to render custom email")
        visible = True
        version = __version__
        category = "FEATURE"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "email_plugin.PluginApp"
