#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import re


VCS_LINK_REGEX = re.compile('\s(?P<commit>#[\d+\w+])\s')


class VcsLinkFilter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        super(VcsLinkFilter, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def get_vcs_link_format(self):
        raise NotImplementedError

    def get_formatted_vcs_link(self, match):
        commit_hash = match.group('commit')
        if commit_hash:
            return self.get_vcs_link_format().format(commit_hash)
        else:
            return None

    def capture_and_replace_commit_token(self, snippet):
        return re.sub(VCS_LINK_REGEX, self.get_formatted_vcs_link, snippet)

# vim: filetype=python
