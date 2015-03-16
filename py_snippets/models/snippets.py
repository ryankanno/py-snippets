#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import BigInteger, String


class Snippet(object):
    __tablename__ = 'snippets'

    id = Column(BigInteger, primary_key=True)
    text = Column(String(256))

    def __init__(self, text=None):
        self.text = text

    def __repr__(self):
        return u"<Snippet %r>".format(self.id)


class SnippetItem(object):
    __tablename__ = 'snippet_items'

    id = Column(BigInteger, primary_key=True)
    type = Column(String(256))

    def __init__(self, type=None):
        self.type = type

    def __repr__(self):
        return u"<Snippet Item (%r)>".format(self.type)


# vim: filetype=python
