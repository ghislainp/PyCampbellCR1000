# -*- coding: utf-8 -*-
"""
PyCampbellCR1000.tests
----------------------

:copyright: Copyright 2012 Salem Harrache and contributors, see AUTHORS.
:license: GNU GPL v3.

"""

from __future__ import unicode_literals

from contextlib import contextmanager

import pytest


@contextmanager
def assert_raises(exception_class, message_part):
    """
    Check that an exception is raised and its message contains some string.
    """
    with pytest.raises(exception_class) as exception:
        yield
    message = "%s" % exception
    assert message_part.lower() in message.lower()
