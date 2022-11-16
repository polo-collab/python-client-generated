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


class Canvas(object):
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
        'mode': 'str'
    }

    attribute_map = {
        'mode': 'mode'
    }

    def __init__(self, mode=None, _configuration=None):  # noqa: E501
        """Canvas - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mode = None
        self.discriminator = None

        self.mode = mode

    @property
    def mode(self):
        """Gets the mode of this Canvas.  # noqa: E501


        :return: The mode of this Canvas.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Canvas.


        :param mode: The mode of this Canvas.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["REAL", "BLOCK", "NOISE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                mode not in allowed_values):
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

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
        if issubclass(Canvas, dict):
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
        if not isinstance(other, Canvas):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Canvas):
            return True

        return self.to_dict() != other.to_dict()
