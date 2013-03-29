from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource


SCHEMES_CSS={
    'red': 'wcc-scheme-red.css',
    'blue': 'wcc-scheme-blue.css',
    'darkgreen': 'wcc-scheme-darkgreen.css'
}

class ColorSchemes(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(SCHEMES_CSS.keys())

grok.global_utility(ColorSchemes, IVocabularyFactory,
                name='wcc.theme.colorscheme')
