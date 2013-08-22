#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import wsme
from wsme import types as wtypes


class APIBase(wtypes.Base):

    def as_dict(self):
      r = {}
      for k in wtypes.inspect_class(self.__class__):
          if getattr(self, k.name) == wsme.Unset:
              continue
          v = getattr(self, k.name)
          if isinstance(v, APIBase):
              v = v.as_dict()
          elif isinstance(v, list):
              v = [a.as_dict() if isinstance(a, APIBase) else a for a in v]
          elif isinstance(v, dict):
              v = dict((k, a.as_dict() if isinstance(a, APIBase) else a)
                      for k, a in v.items())
          r[k.name] = v
      return r
