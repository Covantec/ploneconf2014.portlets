# -*- extra stuff goes here -*-
from zope.i18nmessageid import MessageFactory

portletsMessageFactory = MessageFactory('ploneconf2014.portlets')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
