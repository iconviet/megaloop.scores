# -*- coding: utf-8 -*-
#
# Copyright 2020 ICONVIET
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=W0614
from .megaloop_base import *

"""
Wiring for first SCORE deployment
"""
class Install(MegaloopBase):
    
    def on_install(self):
        super().on_install()
       
        config = Config(self._config.get())
        config.payout_topup = to_loop(5)
        config.payout_ratio = to_percent(100)
        self._config.set(str(config))

        sponsor = self._sponsors.new()
        sponsor.address = str(self.owner)
        self._sponsors[sponsor.address] = sponsor
        
        self._lottery.open(self._block)