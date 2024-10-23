#!/usr/bin/python3

import models.engine.file_storage as fs

# add conditional on HBNB_TYPE_STORAGE
# if equal to db,
#       import DBStorage
#       execute storage.reload()
storage = fs.FileStorage()
storage.reload()
