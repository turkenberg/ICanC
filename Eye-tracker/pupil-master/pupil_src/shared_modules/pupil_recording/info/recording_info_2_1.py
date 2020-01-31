"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2020 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""

from . import RecordingInfoFile, Version
from .recording_info_2_0 import _RecordingInfoFile_2_0
from . import recording_info_utils as utils


class _RecordingInfoFile_2_1(_RecordingInfoFile_2_0):

    # Used for differentiating between < v1.18 and >= v1.18 because of a bug in the
    # upgrade of PI recordings to newstyle. The data format is the same. Note that
    # min_player_version stays the same, as recordings that have been transformed to
    # meta version 2.0 can still be opened with v1.16, but PI recordings opened with
    # meta version 2.0 have to be re-transformed.

    @property
    def meta_version(self) -> Version:
        return Version("2.1")

    @property
    def _private_key_schema(self) -> RecordingInfoFile._KeyValueSchema:
        return {
            **super()._private_key_schema,
            # overwrite meta_version key from parent
            "meta_version": (utils.validator_version_string, lambda _: "2.1"),
        }
