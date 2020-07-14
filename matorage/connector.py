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

from queue import Queue
from minio import Minio
from threading import Thread

from matorage.utils import auto_attr_check

@auto_attr_check
class MRTConnector(object):
    r""" File Storage Connector class with multi-thread.
        MinIO is thread-safety, according to document.
        Although Python Global Interpreter Lock(GIL), multi thread can benefit greatly from file IO.
    """

    _client = Minio
    bucket = str
    num_worker_threads = int

    def __init__(self, client, bucket, num_worker_threads):
        self._client = client
        self._bucket = bucket
        self._queue = Queue()

        for i in range(num_worker_threads):
            _thread = Thread(target=self._worker)
            _thread.daemon = True
            _thread.start()

    def _worker(self):
        while True:
            filename = self._queue.get()
            self.do_job(filename)
            self._queue.task_done()

    def set_queue(self, item):
        self._queue.put(item)

    def join_queue(self):
        self._queue.join()