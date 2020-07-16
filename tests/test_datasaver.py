
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

import unittest
import numpy as np

from tests.test_data import DataTest

from matorage.data.config import DataConfig
from matorage.data.saver import DataSaver
from matorage.data.attribute import DataAttribute

class DataSaverTest(DataTest, unittest.TestCase):

    def test_dataconfig_one_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=DataAttribute('x', 'uint8', (1))
        )

    def test_dataconfig_two_attributes(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'uint8', (1)),
                DataAttribute('y', 'uint8', (1))
            ]
        )

    def test_dataconfig_attributes_already_exist(self):
        with self.assertRaisesRegex(KeyError, 'is already exist in'):
            self.data_config = DataConfig(
                **self.storage_config,
                dataset_name='test_dataconfig',
                attributes=[
                    DataAttribute('x', 'uint8', (1)),
                    DataAttribute('x', 'uint8', (1))
                ]
            )

    def test_dataconfig_string_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'string', (1), itemsize=32)
            ]
        )

    def test_dataconfig_bool_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'bool', (1))
            ]
        )

    def test_dataconfig_int8_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'int8', (1))
            ]
        )

    def test_dataconfig_int16_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'int16', (1))
            ]
        )

    def test_dataconfig_int32_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'int32', (1))
            ]
        )

    def test_dataconfig_uint8_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'uint8', (1))
            ]
        )

    def test_dataconfig_uint16_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'uint16', (1))
            ]
        )


    def test_dataconfig_uint32_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'uint32', (1))
            ]
        )

    def test_dataconfig_uint64_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'uint64', (1))
            ]
        )

    def test_dataconfig_float32_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'float32', (1))
            ]
        )

    def test_dataconfig_float64_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_dataconfig',
            attributes=[
                DataAttribute('x', 'float64', (1))
            ]
        )

    def test_datasaver_string_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'string', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([['a', 'b'], ['c', 'd'], ['e', 'f']])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_bool_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'bool', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[True, False], [False, True], [True, True]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_int8_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'int8', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_int16_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'int16', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_int32_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'int32', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_int64_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'int64', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_uint8_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'uint8', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_uint16_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'uint16', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_uint32_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'uint32', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_uint64_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'uint64', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_float32_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'float32', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })

    def test_datasaver_float64_attribute(self):
        self.data_config = DataConfig(
            **self.storage_config,
            dataset_name='test_datasaver',
            attributes=[
                DataAttribute('x', 'float64', (2), itemsize=32)
            ]
        )
        self.data_saver = DataSaver(
            config=self.data_config
        )
        x = np.asarray([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        self.assertEqual(x.shape, (3, 2))
        self.data_saver({
            'x' : x
        })