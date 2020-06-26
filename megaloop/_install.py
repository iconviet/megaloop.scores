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
from ._scorebase import *

class Install(ScoreBase):
    
    def on_install(self):
        super().on_install()

        topper = self._toppers.create()
        topper.address = str(self.owner)
        self._toppers.save(topper)
        
        config = Config(self._config.get())
        config.draw_topping = to_loop(5)
        config.payout_ratio = to_percent(85)
        self._config.set(str(config))
        
        self._drawbox.open(config, self._instant)