from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource


SCHEMES_CSS={
    'red': 'wcc-waterscheme-red.css',
    'blue': 'wcc-waterscheme-blue.css',
    'darkgreen': 'wcc-waterscheme-darkgreen.css'
}

class ColorSchemes(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(SCHEMES_CSS.keys())

grok.global_utility(ColorSchemes, IVocabularyFactory,
                name='wcc.watertheme.colorscheme')
