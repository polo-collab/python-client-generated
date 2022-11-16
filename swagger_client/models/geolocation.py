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


class Geolocation(object):
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
        'mode': 'str',
        'fill_based_on_external_ip': 'bool',
        'lat': 'float',
        'lng': 'float',
        'accuracy': 'int'
    }

    attribute_map = {
        'mode': 'mode',
        'fill_based_on_external_ip': 'fillBasedOnExternalIp',
        'lat': 'lat',
        'lng': 'lng',
        'accuracy': 'accuracy'
    }

    def __init__(self, mode=None, fill_based_on_external_ip=None, lat=None, lng=None, accuracy=None, _configuration=None):  # noqa: E501
        """Geolocation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mode = None
        self._fill_based_on_external_ip = None
        self._lat = None
        self._lng = None
        self._accuracy = None
        self.discriminator = None

        self.mode = mode
        if fill_based_on_external_ip is not None:
            self.fill_based_on_external_ip = fill_based_on_external_ip
        self.lat = lat
        self.lng = lng
        self.accuracy = accuracy

    @property
    def mode(self):
        """Gets the mode of this Geolocation.  # noqa: E501


        :return: The mode of this Geolocation.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Geolocation.


        :param mode: The mode of this Geolocation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["PROMPT", "BLOCK", "ALLOW"]  # noqa: E501
        if (self._configuration.client_side_validation and
                mode not in allowed_values):
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def fill_based_on_external_ip(self):
        """Gets the fill_based_on_external_ip of this Geolocation.  # noqa: E501


        :return: The fill_based_on_external_ip of this Geolocation.  # noqa: E501
        :rtype: bool
        """
        return self._fill_based_on_external_ip

    @fill_based_on_external_ip.setter
    def fill_based_on_external_ip(self, fill_based_on_external_ip):
        """Sets the fill_based_on_external_ip of this Geolocation.


        :param fill_based_on_external_ip: The fill_based_on_external_ip of this Geolocation.  # noqa: E501
        :type: bool
        """

        self._fill_based_on_external_ip = fill_based_on_external_ip

    @property
    def lat(self):
        """Gets the lat of this Geolocation.  # noqa: E501


        :return: The lat of this Geolocation.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Geolocation.


        :param lat: The lat of this Geolocation.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and lat is None:
            raise ValueError("Invalid value for `lat`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                lat is not None and lat > 90):  # noqa: E501
            raise ValueError("Invalid value for `lat`, must be a value less than or equal to `90`")  # noqa: E501
        if (self._configuration.client_side_validation and
                lat is not None and lat < -90):  # noqa: E501
            raise ValueError("Invalid value for `lat`, must be a value greater than or equal to `-90`")  # noqa: E501

        self._lat = lat

    @property
    def lng(self):
        """Gets the lng of this Geolocation.  # noqa: E501


        :return: The lng of this Geolocation.  # noqa: E501
        :rtype: float
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """Sets the lng of this Geolocation.


        :param lng: The lng of this Geolocation.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and lng is None:
            raise ValueError("Invalid value for `lng`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                lng is not None and lng > 180):  # noqa: E501
            raise ValueError("Invalid value for `lng`, must be a value less than or equal to `180`")  # noqa: E501
        if (self._configuration.client_side_validation and
                lng is not None and lng < -180):  # noqa: E501
            raise ValueError("Invalid value for `lng`, must be a value greater than or equal to `-180`")  # noqa: E501

        self._lng = lng

    @property
    def accuracy(self):
        """Gets the accuracy of this Geolocation.  # noqa: E501


        :return: The accuracy of this Geolocation.  # noqa: E501
        :rtype: int
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        """Sets the accuracy of this Geolocation.


        :param accuracy: The accuracy of this Geolocation.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and accuracy is None:
            raise ValueError("Invalid value for `accuracy`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                accuracy is not None and accuracy < 1):  # noqa: E501
            raise ValueError("Invalid value for `accuracy`, must be a value greater than or equal to `1`")  # noqa: E501

        self._accuracy = accuracy

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
        if issubclass(Geolocation, dict):
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
        if not isinstance(other, Geolocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Geolocation):
            return True

        return self.to_dict() != other.to_dict()