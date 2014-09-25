#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import VcsLinkFilter


class BitBucketLinkFilter(VcsLinkFilter):

    def __init__(self, repo, *args, **kwargs):
        super(BitBucketLinkFilter, self).__init__(*args, **kwargs)
        self.repo = repo

    @property
    def repo(self):
        return self._repo

    @repo.setter
    def repo(self, value):
        self._repo = value

    def get_vcs_link_format(self):
        return "https://bitbucket.org/" + self.repo + "/commits/{0}"

# vim: filetype=python
