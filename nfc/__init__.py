# -*- coding: latin-1 -*-
# -----------------------------------------------------------------------------
# Copyright 2009, 2017 Stephen Tiedemann <stephen.tiedemann@gmail.com>
#
# Licensed under the EUPL, Version 1.1 or - as soon they 
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/software/page/eupl
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
# -----------------------------------------------------------------------------
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
logging.getLogger(__name__).setLevel(logging.INFO)

from clf import ContactlessFrontend

# METADATA ####################################################################

__version__ = "latest"

__title__ = "nfcpy"
__description__ = "Python module for Near Field Communication."
__uri__ = "https://github.com/nfcpy/nfcpy"

__author__ = "Stephen Tiedemann"
__email__ = "stephen.tiedemann@gmail.com"

__license__ = "EUPL"
__copyright__ = "Copyright (c) 2009, 2017 Stephen Tiedemann"

###############################################################################
