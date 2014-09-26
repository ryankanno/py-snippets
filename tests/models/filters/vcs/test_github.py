#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from py_snippets.models.filters.vcs.github import GithubLinkFilter
import unittest


class TestGithubLinkFilter(unittest.TestCase):

    def test_github_link_filter_object(self):
        repo = "ryankanno/foobar"
        filter = GithubLinkFilter(repo)
        ok_(filter.repo == repo)
        ok_(filter.get_vcs_link_format()
            == "https://github.com/ryankanno/foobar/commit/{0}")
# vim: filetype=python
