# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from inductiva.client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ADMIN = "admin"
    COMPUTE = "compute"
    EXECUTERTRACKERS = "executer-trackers"
    STORAGE = "storage"
    TASKS = "tasks"
    VERSION = "version"