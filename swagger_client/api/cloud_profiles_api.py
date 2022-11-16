# coding: utf-8

"""
    Multilogin v2 Local API

    This API is intended to be used from version 5 of Multilogin for managing cloud saved browser profiles.   To start/stop browser profiles please use the [Multilogin v1 Local API](https://app.swaggerhub.com/apis/Multilogin/MultiloginLocalRestAPI/1.0). # Creating profiles To create a profile send a POST request to the /profile endpoint. The mandatory parameters are the name of the profile, operating system and type of browser. The rest of the fingerprint will be generated automatically, unless you specify more details.  Here is an example request to create a Mimic profile for windows with a proxy: <pre>{ <br>\"name\": \"testProfile\", <br>\"browser\": \"mimic\", <br>\"os\": \"win\", <br>\"network\": { <br>    \"proxy\": { <br>        \"type\": \"HTTP\", <br>        \"host\": \"192.168.1.1\", <br>        \"port\": \"1080\", <br>        \"username\": \"username\", <br>        \"password\": \"password\" <br>        } <br>    } <br>} </pre> # Groups Each group has an unique ID that can be assigned either during the creating of a profile or by updating a profile.  The default group ID is 00000000-0000-0000-0000-000000000000 for Unassigned  # noqa: E501

    OpenAPI spec version: v2-beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CloudProfilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def profile_get(self, **kwargs):  # noqa: E501
        """listProfiles  # noqa: E501

        Returns a list of profiles as a JSON array.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.profile_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def profile_get_with_http_info(self, **kwargs):  # noqa: E501
        """listProfiles  # noqa: E501

        Returns a list of profiles as a JSON array.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profile_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/profile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse200]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profile_post(self, body, **kwargs):  # noqa: E501
        """createProfile  # noqa: E501

        Create a new browser profile. Required fields to be passed in the body are: Name, OS, Browser. All the fields not passed in the body are generated automatically. Returns the ID of the newly created profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Profile body: (required)
        :param int browser_version_min: Minimum browser version
        :param int browser_version_max: Maximum browser version
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def profile_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """createProfile  # noqa: E501

        Create a new browser profile. Required fields to be passed in the body are: Name, OS, Browser. All the fields not passed in the body are generated automatically. Returns the ID of the newly created profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Profile body: (required)
        :param int browser_version_min: Minimum browser version
        :param int browser_version_max: Maximum browser version
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'browser_version_min', 'browser_version_max']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profile_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `profile_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'browser_version_min' in params:
            query_params.append(('browserVersionMin', params['browser_version_min']))  # noqa: E501
        if 'browser_version_max' in params:
            query_params.append(('browserVersionMax', params['browser_version_max']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/profile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profile_uuid_delete(self, uuid, **kwargs):  # noqa: E501
        """removeProfile  # noqa: E501

        Deletes the profile permanently  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_delete(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_delete_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_delete_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def profile_uuid_delete_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """removeProfile  # noqa: E501

        Deletes the profile permanently  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_delete_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profile_uuid_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `profile_uuid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/profile/{uuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profile_uuid_migrate_post(self, uuid, **kwargs):  # noqa: E501
        """migrateProfile  # noqa: E501

        Migrates the profile from version 4.x to 5.x  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_migrate_post(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_migrate_post_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_migrate_post_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def profile_uuid_migrate_post_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """migrateProfile  # noqa: E501

        Migrates the profile from version 4.x to 5.x  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_migrate_post_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profile_uuid_migrate_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `profile_uuid_migrate_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/profile/{uuid}/migrate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profile_uuid_post(self, uuid, body, **kwargs):  # noqa: E501
        """updateProfile  # noqa: E501

        Updates the profile based on the JSON passed in the body. OS and browser type can not be changed   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_post(uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile ID (required)
        :param UpdateProfileExample body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_post_with_http_info(uuid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_post_with_http_info(uuid, body, **kwargs)  # noqa: E501
            return data

    def profile_uuid_post_with_http_info(self, uuid, body, **kwargs):  # noqa: E501
        """updateProfile  # noqa: E501

        Updates the profile based on the JSON passed in the body. OS and browser type can not be changed   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_post_with_http_info(uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile ID (required)
        :param UpdateProfileExample body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profile_uuid_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `profile_uuid_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `profile_uuid_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/profile/{uuid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profile_uuid_update_post(self, uuid, **kwargs):  # noqa: E501
        """updateProfileCore  # noqa: E501

        Updates the browser core to the latest version  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_update_post(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_update_post_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_update_post_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def profile_uuid_update_post_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """updateProfileCore  # noqa: E501

        Updates the browser core to the latest version  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_update_post_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profile_uuid_update_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and ('uuid' not in params or
                                                       params['uuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uuid` when calling `profile_uuid_update_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/profile/{uuid}/update', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)