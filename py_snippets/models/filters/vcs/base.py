#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class VcsLinkFilter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        super(VcsLinkFilter, self).__init__(*args, **kwargs)

# vim: filetype=python
