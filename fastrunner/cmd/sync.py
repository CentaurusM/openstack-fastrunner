# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Starter script for Fastrunner API.
"""

import sys

from oslo_config import cfg
from oslo_log import log as logging
from oslo_reports import guru_meditation_report as gmr
import six

from fastrunner import config
from fastrunner import service
from fastrunner.sync import sync_service
from fastrunner import version

CONF = cfg.CONF


def main():
    config.parse_args(sys.argv)
    logging.setup(CONF, "fastrunner")
    log = logging.getLogger(__name__)
    gmr.TextGuruMeditation.setup_autorun(version)


    server = sync_service.SyncService()
    service.serve(server)
    service.wait()

if __name__ == "__main__":
    sys.exit(main())