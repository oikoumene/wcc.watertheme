from zope import schema
from zope.interface import Interface

class IThemeSettings(Interface):
    scheme = schema.Choice(title=u"Color scheme",
            vocabulary="wcc.theme.colorscheme",
            default='red')

class IThemeSpecific(Interface):
    pass
