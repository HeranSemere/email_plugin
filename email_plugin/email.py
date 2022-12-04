from pretix.base.email import TemplateBasedMailRenderer

class MyMailRenderer(TemplateBasedMailRenderer):
    verbose_name = ('Arifpay design')
    identifier = 'email_plugin'
    thumbnail_filename = 'pretixbase/email/thumb.png'
    template_name = 'pretixbase/email/plainwrapper.html'
    