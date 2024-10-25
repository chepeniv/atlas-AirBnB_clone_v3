#!/usr/bin/python3

import os


storage_type = os.environ.get('HBNB_TYPE_STORAGE', 'file')

if storage_type == 'db':
    import models.engine.DBStorage as fs
else:
    import models.engine.file_storage as fs

storage = fs()
storage.reload()

