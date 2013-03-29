from collective.grok import gs
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from wcc.watertheme.interfaces import IThemeSettings

@gs.importstep(
    name=u'wcc.watertheme',
    title='wcc.watertheme import handler',
    description='')
def setupVarious(context):
    if context.readDataFile('wcc.watertheme.marker.txt') is None:
        return
    portal = context.getSite()
    registry = getUtility(IRegistry)
    registry.registerInterface(IThemeSettings)
