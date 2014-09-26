#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import VcsLinkFilter


class GithubLinkFilter(VcsLinkFilter):

    def __init__(self, repo, *args, **kwargs):
        super(GithubLinkFilter, self).__init__(*args, **kwargs)
        self.repo = repo

    @property
    def repo(self):
        return self._repo

    @repo.setter
    def repo(self, value):
        self._repo = value

    def get_vcs_link_format(self):
        return "https://github.com/{repo}/commit/{{0}}".format(repo=self.repo)

# vim: filetype=python
