#!/usr/bin/env python
# coding: utf-8

"""
OutputApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from .. import configuration
from ..api_client import ApiClient

class OutputApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('http://api2.online-convert.com')
            self.api_client = configuration.api_client
    
    
    def jobs_job_id_output_get(self, job_id, **kwargs):
        """
        Get list of converted.
        

        :param str conversion_id:  
        :param str input_id:  
        :param str token: Token for authentication. 
        :param str key: Api key for the user to filter. 
        :param str job_id: ID of job that needs to be fetched (required)
        
        :return: list[OutputFile]
        """
        
        # verify the required parameter 'job_id' is set
        if job_id is None:
            raise ValueError("Missing the required parameter `job_id` when calling `jobs_job_id_output_get`")
        
        all_params = ['conversion_id', 'input_id', 'token', 'key', 'job_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_output_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs/{job_id}/output'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  
        
        query_params = {}
        
        if 'conversion_id' in params:
            query_params['conversion_id'] = params['conversion_id']
        
        if 'input_id' in params:
            query_params['input_id'] = params['input_id']
        
        header_params = {}
        
        if 'token' in params:
            header_params['token'] = params['token']
        
        if 'key' in params:
            header_params['key'] = params['key']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='list[OutputFile]', auth_settings=auth_settings)
        
        return response
        
    def jobs_job_id_output_file_id_get(self, job_id, file_id, **kwargs):
        """
        Get information about an output file source.
        

        :param str token: Token for authentication. 
        :param str key: Api key for the user to filter. 
        :param str job_id: ID of job that needs to be fetched (required)
        :param str file_id: Id of the file to download (required)
        
        :return: list[OutputFile]
        """
        
        # verify the required parameter 'job_id' is set
        if job_id is None:
            raise ValueError("Missing the required parameter `job_id` when calling `jobs_job_id_output_file_id_get`")
        
        # verify the required parameter 'file_id' is set
        if file_id is None:
            raise ValueError("Missing the required parameter `file_id` when calling `jobs_job_id_output_file_id_get`")
        
        all_params = ['token', 'key', 'job_id', 'file_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_output_file_id_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs/{job_id}/output/{file_id}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  
        
        if 'file_id' in params:
            path_params['file_id'] = params['file_id']  
        
        query_params = {}
        
        header_params = {}
        
        if 'token' in params:
            header_params['token'] = params['token']
        
        if 'key' in params:
            header_params['key'] = params['key']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='list[OutputFile]', auth_settings=auth_settings)
        
        return response
        
    def jobs_job_id_output_file_id_delete(self, job_id, file_id, **kwargs):
        """
        Deletes a file from the output.
        

        :param str token: Token for authentication. 
        :param str key: Api key for the user to filter. 
        :param str job_id: ID of job that needs to be fetched (required)
        :param str file_id: Id of the file to download (required)
        
        :return: list[OutputFile]
        """
        
        # verify the required parameter 'job_id' is set
        if job_id is None:
            raise ValueError("Missing the required parameter `job_id` when calling `jobs_job_id_output_file_id_delete`")
        
        # verify the required parameter 'file_id' is set
        if file_id is None:
            raise ValueError("Missing the required parameter `file_id` when calling `jobs_job_id_output_file_id_delete`")
        
        all_params = ['token', 'key', 'job_id', 'file_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_output_file_id_delete" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs/{job_id}/output/{file_id}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  
        
        if 'file_id' in params:
            path_params['file_id'] = params['file_id']  
        
        query_params = {}
        
        header_params = {}
        
        if 'token' in params:
            header_params['token'] = params['token']
        
        if 'key' in params:
            header_params['key'] = params['key']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='list[OutputFile]', auth_settings=auth_settings)
        
        return response
        









