#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import VcsLinkFilter

class BitBucketLinkFilter(VcsLinkFilter):

    def __init__(self, *args, **kwargs):
        super(BitBucketLinkFilter, self).__init__(*args, **kwargs)

# vim: filetype=python
