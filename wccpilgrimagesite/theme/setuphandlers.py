from collective.grok import gs
from wccpilgrimagesite.theme import MessageFactory as _

@gs.importstep(
    name=u'wccpilgrimagesite.theme', 
    title=_('wccpilgrimagesite.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wccpilgrimagesite.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
