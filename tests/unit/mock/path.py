from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import (
    MagicMock,
)
from ansible.utils.path import unfrackpath


mock_unfrackpath_noop = MagicMock(
    spec_set=unfrackpath, side_effect=lambda x, *args, **kwargs: x
)
