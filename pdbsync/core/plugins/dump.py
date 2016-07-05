# !/usr/bin/env python
# coding=utf8

from pdbsync.core import logger


class PyDumps(object):
    def __init__(self, dbs):
        self.dbs = dbs

    def run(self):
        for db in self.dbs:
            logger.info("db: %s" % db)

            pydump = PyDump(db.src, db.dest)
            pydump.run()


class PyDump(object):
    def __init__(self, src_db, dest_db):
        self.src_db = src_db
        self.dest_db = dest_db

    def run(self):
        src_db = self.src_db
        dest_db = self.dest_db
        command = "mysqldump -h %s -P %s -u%s -p%s %s | mysql -h %s -P %s -u%s -p%s %s" % \
                  (src_db.host, src_db.port, src_db.username, src_db.password, src_db.db_name,
                   dest_db.host, dest_db.port, dest_db.username, dest_db.password, dest_db.db_name)

        logger.info(command)