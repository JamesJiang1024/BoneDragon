# -*- encoding: utf-8 -*-
#
# Copyright © 2013 Unitedstack Inc.
#
# Author: Jianing YANG (jianingy@unitedstack.com)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""A middleware that turns exceptions into parsable string.
"""

import json
import sys
import traceback
import webob
import webob.dec


class Fault(object):

    def __init__(self, exc):
        self.exc = exc
        exc_info = sys.exc_info()
        if exc_info[2]:
            self.traceback = traceback.format_exc(exc_info[2])
        else:
            self.traceback = ''
        self.error_dict = {
            'message': str(exc),
            'error': {
                'traceback': self.traceback
            }
        }

    @webob.dec.wsgify
    def __call__(self, req):
        error_body = json.dumps(self.error_dict)
        resp = webob.Response(body=error_body, request=req)
        resp.headers.add('Content-Type', 'application/json')
        default_webob_exc = webob.exc.HTTPInternalServerError()
        resp.status_code = getattr(self.exc, 'code', default_webob_exc.code)
        return resp


class FaultWrapperMiddleware(object):

    def __init__(self, app):
        self.app = app

    @webob.dec.wsgify
    def __call__(self, req):
        try:
            return req.get_response(self.app)
        except Exception as exc:
            return req.get_response(Fault(exc))
