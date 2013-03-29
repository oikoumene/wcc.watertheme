from collective.grok import gs
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from wcc.theme.interfaces import IThemeSettings

@gs.importstep(
    name=u'wcc.theme',
    title='wcc.theme import handler',
    description='')
def setupVarious(context):
    if context.readDataFile('wcc.theme.marker.txt') is None:
        return
    portal = context.getSite()
    registry = getUtility(IRegistry)
    registry.registerInterface(IThemeSettings)
