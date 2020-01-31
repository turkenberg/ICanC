"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2020 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""

"""
Video Capture provides the interface to get frames from diffferent backends.
Backends consist of a manager and at least one source class. The manager
is a Pupil plugin that provides an GUI that lists all available sources. The
source provides the stream of image frames.

These backends are available:
- UVC: Local USB sources
- NDSI: Remote Pupil Mobile sources
- Fake: Fallback, static grid image
- File: Loads video from file
"""

import logging
import os
from glob import glob

import numpy as np

from camera_models import load_intrinsics

from .base_backend import (
    Base_Manager,
    Base_Source,
    EndofVideoError,
    InitialisationError,
    StreamError,
)
from .fake_backend import Fake_Manager, Fake_Source
from .file_backend import File_Manager, File_Source, FileSeekError
from .hmd_streaming import HMD_Streaming_Source
from .uvc_backend import UVC_Manager, UVC_Source

logger = logging.getLogger(__name__)


source_classes = [File_Source, UVC_Source, Fake_Source, HMD_Streaming_Source]
manager_classes = [File_Manager, UVC_Manager, Fake_Manager]

try:
    from .ndsi_backend import NDSI_Source, NDSI_Manager
except ImportError:
    logger.info("Install pyndsi to use the Pupil Mobile backend")
else:
    source_classes.append(NDSI_Source)
    manager_classes.append(NDSI_Manager)

try:
    from .realsense_backend import Realsense_Source, Realsense_Manager
except ImportError:
    logger.debug("Install pyrealsense to use the Intel RealSense backend")
else:
    source_classes.append(Realsense_Source)
    manager_classes.append(Realsense_Manager)

try:
    from .realsense2_backend import Realsense2_Source, Realsense2_Manager
except ImportError:
    logger.debug(
        "Install pyrealsense2 to use the Intel RealSense backend for D400 series cameras"
    )
else:
    source_classes.append(Realsense2_Source)
    manager_classes.append(Realsense2_Manager)