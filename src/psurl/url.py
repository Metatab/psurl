# Copyright (c) 2019 Civic Knowledge. This file is licensed under the terms of the
# MIT, included in this distribution as LICENSE

"""Baseclass for urls. """

from furl import furl
from furl.common import absent as _absent

class PsUrl(object):
    """Baseclass for all PSURLS"""

    inner: furl

    def __init__(self) -> None:
        super().__init__()

    def reparse(self):
        raise NotImplementedError()

    def rewrite(self):
        raise NotImplementedError()

    def fetch(self):
        raise NotImplementedError()

    def extract(self):
        raise NotImplementedError()

    def resolve(self):
        """Return the URL of the downloaded an fully extracted verion of the resource"""
        raise NotImplementedError()

class CustomUrl(PsUrl):

    def rewrite(self):
        pass

class WebUrl(PsUrl):

    def fetch(self):
        pass


class LocalUrl(PsUrl):
    pass

class LocalArchiveUrl(LocalUrl):

    def extract(self):
        pass


class LocalFileUrl(LocalUrl):
    pass