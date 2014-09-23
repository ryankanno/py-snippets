#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import VcsLinkFilter


class GithubLinkFilter(VcsLinkFilter):

    def __init__(self, *args, **kwargs):
        super(GithubLinkFilter, self).__init__(*args, **kwargs)

# vim: filetype=python
