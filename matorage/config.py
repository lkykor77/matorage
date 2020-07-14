
# Original Code
# https://github.com/huggingface/transformers/blob/master/src/transformers/configuration_utils.py
# See https://github.com/graykode/matorage/blob/0.1.0/NOTICE
# modified by TaeHwan Jung(@graykode)

# Copyright 2020-present Tae Hwan Jung
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import copy

_KB = 1024
"""The size of a Kilobyte in bytes"""

_MB = 1024 * _KB
"""The size of a Megabyte in bytes"""

class MTRConfig(object):
    r""" Storage connector configuration classes.
        Handles a few parameters configuration for backend storage, hdf5 and etc.

        Args:
            For MinIO, see [this page](https://docs.min.io/docs/python-client-api-reference.html) for more details.
            MinIO Options
                endpoint (:obj:`string`, `require`):
                    S3 object storage endpoint.
                access_key (:obj:`string`, `optional`, defaults to `None`):
                    Access key for the object storage endpoint. (Optional if you need anonymous access).
                secret_key (:obj:`string`, `optional`, defaults to `None`):
                    Secret key for the object storage endpoint. (Optional if you need anonymous access).
                secure (:obj:`bool`, `optional`, defaults to `False`):
                    Set this value to True to enable secure (HTTPS) access. (Optional defaults to False unlike the original MinIO).
                min_object_size (:obj:`int`, `optional`, defaults to `10 * 1024 * 1024`):
                    The minimum size of object storage stored as an actual object.
                max_object_size (:obj:`int`, `optional`, defaults to `100 * 1024 * 1024`):
                    The maximum size of object storage stored as an actual object.
                multipart_upload_size (:obj:`int`, `optional`, defaults to `10 * 1024 * 1024`):
                    size of the incompletely uploaded object.
                    You can sync files faster with multipart upload in MinIO.
                    (https://github.com/minio/minio-py/blob/master/minio/api.py#L1795)
                    This is because MinIO clients use multi-threading, which improves IO speed more
                    efficiently regardless of Python's Global Interpreter Lock(GIL).
                multipart_upload_size (:obj:`int`, `optional`, defaults to `5 * 1024 * 1024`):
                    size of the incompletely uploaded object.
                num_worker_threads :obj:`int`, `optional`, defaults to `4`):
                    number of backend storage worker to upload or download.

            HDF5 Options
                inmemory (:obj:`bool`, `optional`, defaults to `False`):
                    If you use this value as `True`, then you can use `HDF5_CORE` driver (https://support.hdfgroup.org/HDF5/doc/TechNotes/VFL.html#TOC1)
                    so the temporary file for uploading or downloading to backend storage,
                    such as MinIO, is not stored on disk but is in the memory.
                    Keep in mind that using memory is fast because it doesn't use disk IO, but it's not always good.
                    If default option(False), then `HDF5_SEC2` driver will be used on posix OS(or `HDF5_WINDOWS` in Windows).

    """

    def __init__(self, **kwargs):

        # MinIO configuration
        self.endpoint = kwargs.pop("endpoint", None)
        self.access_key = kwargs.pop("access_key", None)
        self.secret_key = kwargs.pop("secret_key", None)
        self.secure = kwargs.pop("secure", False)
        self.min_object_size = kwargs.pop("min_object_size", 10 * _MB)
        self.max_object_size = kwargs.pop("max_object_size", 100 * _MB)
        self.multipart_upload_size = kwargs.pop("multipart_upload_size", 5 * _MB)
        self.num_worker_threads = kwargs.pop("num_worker_threads", 4)

        # HDF5 configuration
        self.inmemory = kwargs.pop("inmemory", False)

    def __repr__(self):
        return "{} {}".format(self.__class__.__name__, self._to_json_string())

    def _to_dict(self):
        """
        Serializes this instance to a Python dictionary.

        Returns:
            :obj:`Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
        output = copy.deepcopy(self.__dict__)
        return output

    def _to_json_string(self):
        """
        Serializes this instance to a JSON string.

        Returns:
            :obj:`string`: String containing all the attributes that make up this configuration instance in JSON format.
        """
        return json.dumps(self._to_dict(), indent=4, sort_keys=True) + "\n"

    def to_json_file(self, json_file_path, use_diff=True):
        """
        Save this instance to a json file.

        Args:
            json_file_path (:obj:`string`):
                Path to the JSON file in which this configuration instance's parameters will be saved.
            use_diff (:obj:`bool`):
                If set to True, only the difference between the config instance and the default PretrainedConfig() is serialized to JSON file.
        """
        with open(json_file_path, "w", encoding="utf-8") as writer:
            writer.write(self._to_json_string(use_diff=use_diff))