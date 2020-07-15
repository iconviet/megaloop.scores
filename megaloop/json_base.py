# -*- coding: utf-8 -*-

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
from iconservice import *
"""
Base class for JSON object
"""
class JsonBase(object):
    
    def __init__(self, json:str=None):
        if json: self.load(json)

    def __repr__(self):
        return json_dumps(self.__dict__)

    def load(self, json:str):
        if json: self.__dict__.update(json_loads(json))