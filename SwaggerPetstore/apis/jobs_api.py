#!/usr/bin/env python
# coding: utf-8

"""
JobsApi.py
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

class JobsApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('http://api2.online-convert.com')
            self.api_client = configuration.api_client
    
    
    def jobs_get(self, **kwargs):
        """
        List of jobs active for the current user identified by the key.
        It will return the list of jobs for the given user. In order to get the jobs a key or token must be provided:\n  - If the user key is provided all jobs for the current will be return.\n  - If one token is provided it will return the job assigned to that token if any.\n  \nThe request is paginated with an amount of 50 elements per page in any case.\n

        :param str status: Filter the status of the job. 
        :param str token: Token for authentication. 
        :param str key: Api key for the user to filter. 
        :param Number page: Pagination for list of elements. 
        
        :return: list[Job]
        """
        
        all_params = ['status', 'token', 'key', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'status' in params:
            query_params['status'] = params['status']
        
        if 'page' in params:
            query_params['page'] = params['page']
        
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
                                            response='list[Job]', auth_settings=auth_settings)
        
        return response
        
    def jobs_post(self, key, body, **kwargs):
        """
        Creates a new Job with the user key.
        

        :param str key: Api key for the user to filter. (required)
        :param Job body: Content of the job. (required)
        
        :return: Job
        """
        
        # verify the required parameter 'key' is set
        if key is None:
            raise ValueError("Missing the required parameter `key` when calling `jobs_post`")
        
        # verify the required parameter 'body' is set
        if body is None:
            raise ValueError("Missing the required parameter `body` when calling `jobs_post`")
        
        all_params = ['key', 'body']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        if 'key' in params:
            header_params['key'] = params['key']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'body' in params:
            body_params = params['body']
        
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
                                            response='Job', auth_settings=auth_settings)
        
        return response
        
    def jobs_job_id_get(self, job_id, **kwargs):
        """
        Get information about a Job
        

        :param str token: Token for authentication. 
        :param str key: Api key for the user to filter. 
        :param str job_id: ID of job that needs to be fetched (required)
        
        :return: Job
        """
        
        # verify the required parameter 'job_id' is set
        if job_id is None:
            raise ValueError("Missing the required parameter `job_id` when calling `jobs_job_id_get`")
        
        all_params = ['token', 'key', 'job_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs/{job_id}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  
        
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
                                            response='Job', auth_settings=auth_settings)
        
        return response
        
    def jobs_job_id_delete(self, job_id, **kwargs):
        """
        Cancels a job created that haven't been started. (Allow to cancel jobs in process.)
        

        :param str token: Token for authentication. 
        :param str key: Api key for the user to filter. 
        :param str job_id: ID of job that needs to be fetched (required)
        
        :return: Job
        """
        
        # verify the required parameter 'job_id' is set
        if job_id is None:
            raise ValueError("Missing the required parameter `job_id` when calling `jobs_job_id_delete`")
        
        all_params = ['token', 'key', 'job_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_delete" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs/{job_id}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  
        
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
                                            response='Job', auth_settings=auth_settings)
        
        return response
        
    def jobs_job_id_patch(self, body, job_id, **kwargs):
        """
        Modifies the job identified by the id, allows to start a created job.
        

        :param Job body: Content of the job. (required)
        :param str token: Token for authentication. 
        :param str key: Api key for the user to filter. 
        :param str job_id: ID of job that needs to be fetched (required)
        
        :return: Job
        """
        
        # verify the required parameter 'body' is set
        if body is None:
            raise ValueError("Missing the required parameter `body` when calling `jobs_job_id_patch`")
        
        # verify the required parameter 'job_id' is set
        if job_id is None:
            raise ValueError("Missing the required parameter `job_id` when calling `jobs_job_id_patch`")
        
        all_params = ['body', 'token', 'key', 'job_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_patch" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs/{job_id}'.replace('{format}', 'json')
        method = 'PATCH'

        path_params = {}
        
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  
        
        query_params = {}
        
        header_params = {}
        
        if 'token' in params:
            header_params['token'] = params['token']
        
        if 'key' in params:
            header_params['key'] = params['key']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'body' in params:
            body_params = params['body']
        
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
                                            response='Job', auth_settings=auth_settings)
        
        return response
        
    def jobs_job_id_threads_get(self, job_id, **kwargs):
        """
        Get list of threads defined for the current job.
        

        :param str token: Token for authentication. 
        :param str key: Api key for the user to filter. 
        :param str job_id: ID of job that needs to be fetched (required)
        
        :return: list[Thread]
        """
        
        # verify the required parameter 'job_id' is set
        if job_id is None:
            raise ValueError("Missing the required parameter `job_id` when calling `jobs_job_id_threads_get`")
        
        all_params = ['token', 'key', 'job_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method jobs_job_id_threads_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/jobs/{job_id}/threads'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  
        
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
                                            response='list[Thread]', auth_settings=auth_settings)
        
        return response
        









