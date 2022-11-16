# coding: utf-8

"""
    Multilogin v2 Local API

    This API is intended to be used from version 5 of Multilogin for managing cloud saved browser profiles.   To start/stop browser profiles please use the [Multilogin v1 Local API](https://app.swaggerhub.com/apis/Multilogin/MultiloginLocalRestAPI/1.0). # Creating profiles To create a profile send a POST request to the /profile endpoint. The mandatory parameters are the name of the profile, operating system and type of browser. The rest of the fingerprint will be generated automatically, unless you specify more details.  Here is an example request to create a Mimic profile for windows with a proxy: <pre>{ <br>\"name\": \"testProfile\", <br>\"browser\": \"mimic\", <br>\"os\": \"win\", <br>\"network\": { <br>    \"proxy\": { <br>        \"type\": \"HTTP\", <br>        \"host\": \"192.168.1.1\", <br>        \"port\": \"1080\", <br>        \"username\": \"username\", <br>        \"password\": \"password\" <br>        } <br>    } <br>} </pre> # Groups Each group has an unique ID that can be assigned either during the creating of a profile or by updating a profile.  The default group ID is 00000000-0000-0000-0000-000000000000 for Unassigned  # noqa: E501

    OpenAPI spec version: v2-beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class UpdateProfileExample(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'group': 'str',
        'network': 'UpdateProfileExampleNetwork'
    }

    attribute_map = {
        'name': 'name',
        'group': 'group',
        'network': 'network'
    }

    def __init__(self, name=None, group=None, network=None, _configuration=None):  # noqa: E501
        """UpdateProfileExample - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._group = None
        self._network = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if group is not None:
            self.group = group
        if network is not None:
            self.network = network

    @property
    def name(self):
        """Gets the name of this UpdateProfileExample.  # noqa: E501

        Name of the profile  # noqa: E501

        :return: The name of this UpdateProfileExample.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateProfileExample.

        Name of the profile  # noqa: E501

        :param name: The name of this UpdateProfileExample.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group(self):
        """Gets the group of this UpdateProfileExample.  # noqa: E501

        Group ID where profile is assigned to  # noqa: E501

        :return: The group of this UpdateProfileExample.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UpdateProfileExample.

        Group ID where profile is assigned to  # noqa: E501

        :param group: The group of this UpdateProfileExample.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def network(self):
        """Gets the network of this UpdateProfileExample.  # noqa: E501


        :return: The network of this UpdateProfileExample.  # noqa: E501
        :rtype: UpdateProfileExampleNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this UpdateProfileExample.


        :param network: The network of this UpdateProfileExample.  # noqa: E501
        :type: UpdateProfileExampleNetwork
        """

        self._network = network

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateProfileExample, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateProfileExample):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateProfileExample):
            return True

        return self.to_dict() != other.to_dict()