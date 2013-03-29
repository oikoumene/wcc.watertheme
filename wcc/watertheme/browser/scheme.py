from five import grok
from zope.interface import Interface
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from wcc.watertheme.interfaces import IThemeSettings
from wcc.watertheme.vocabulary import SCHEMES_CSS
from zope.component.hooks import getSite

class SchemeCSS(grok.View):
    grok.context(Interface)
    grok.name('wcc-watertheme-scheme.css')

    def render(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IThemeSettings)
        self.request.response.setHeader('Content-Type','text/css; charset=utf-8')
        scheme_css = SCHEMES_CSS[settings.scheme]
        site = getSite()
        result = getattr(site, scheme_css)
        return unicode(result)
