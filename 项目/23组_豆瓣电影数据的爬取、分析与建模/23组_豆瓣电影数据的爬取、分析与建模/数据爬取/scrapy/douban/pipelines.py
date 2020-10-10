#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 23:41:38 2019

@author: liudiwei
"""

import hashlib

import douban.database as db

from douban.items import Comment, BookMeta, MovieMeta, Subject,PersonMeta

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.misc import arg_to_iter
from scrapy.utils.python import to_bytes

from twisted.internet.defer import DeferredList

cursor = db.connection.cursor()


class DoubanPipeline(object):
    def get_subject(self, item):
        if item["douban_id"] == "":
            print("Get Subject Exception: douban_id is null.")
        #else:

        sql = 'SELECT id FROM subjects WHERE douban_id=%s' % item['douban_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_subject(self, item):
        if item["douban_id"] == "":
            print("Save Subject Exception: douban_id is null.")
        else:
            keys = item.keys()
            values = tuple(item.values())
            fields = ','.join(keys)
            temp = ','.join(['%s'] * len(keys))
            sql = 'INSERT INTO subjects (%s) VALUES (%s)' % (fields, temp)
            cursor.execute(sql, values)
            return db.connection.commit()

    def get_movie_meta(self, item):
        sql = 'SELECT id FROM movies WHERE douban_id=%s' % item['douban_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_movie_meta(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO movies (%s) VALUES (%s)' % (fields, temp)
        print("##save## save_movie_meta: ", sql)

        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()

    def update_movie_meta(self, item):
        douban_id = item.pop('douban_id')
        keys = item.keys()
        values = tuple(item.values())
        #values.append(douban_id)
        fields = ['%s=' % i + '%s' for i in keys]
        sql = 'UPDATE movies SET %s WHERE douban_id=%s' % (','.join(fields), douban_id)
        print("##update## update_movie_meta: ", sql)
        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()


    def get_person_meta(self, item):
        sql = 'SELECT id FROM person WHERE person_id=%s' % item['person_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_person_meta(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO person (%s) VALUES (%s)' % (fields, temp)
        print("##save## save_person_meta: ", sql)

        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()

    def update_person_meta(self, item):
        person_id = item.pop('person_id')
        keys = item.keys()
        values = tuple(item.values())
        #values.append(douban_id)
        fields = ['%s=' % i + '%s' for i in keys]
        sql = 'UPDATE person SET %s WHERE person_id=%s' % (','.join(fields), person_id)
        print("##update## update_person_meta: ", sql)
        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()

    def get_book_meta(self, item):
        sql = 'SELECT id FROM books WHERE douban_id=%s' % item['douban_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_book_meta(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO books (%s) VALUES (%s)' % (fields, temp)
        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()

    def update_book_meta(self, item):
        douban_id = item.pop('douban_id')
        keys = item.keys()
        values = tuple(item.values())
        values.append(douban_id)
        fields = ['%s=' % i + '%s' for i in keys]
        sql = 'UPDATE books SET %s WHERE douban_id=%s' % (','.join(fields), '%s')
        cursor.execute(sql, values)
        return db.connection.commit()

    def get_comment(self, item):
        sql = 'SELECT * FROM comments WHERE douban_comment_id=%s\
' % item['douban_comment_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_comment(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO comments (%s) VALUES (%s)' % (fields, temp)
        cursor.execute(sql, values)
        return db.connection.commit()

    def update_comment(self, item):
        douban_comment_id = item.pop('douban_comment_id')
        keys = item.keys()
        values = tuple(item.values())
        #values.append(douban_id)
        fields = ['%s=' % i + '%s' for i in keys]
        sql = 'UPDATE comments SET %s WHERE douban_comment_id=%s' % (','.join(fields), douban_comment_id)
        print("##update## update_comment: ", sql)
        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()

    def process_item(self, item, spider):
        if isinstance(item, Subject):
            '''
            subject
            '''
            exist = self.get_subject(item)
            if not exist:
                self.save_subject(item)
        elif isinstance(item, MovieMeta):
            '''
            meta
            '''
            exist = self.get_movie_meta(item)
            if not exist:
                try:
                    self.save_movie_meta(item)
                except Exception as e:
                    print(item)
                    print(e)
            else:
                self.update_movie_meta(item)
        elif isinstance(item, BookMeta):
            '''
            meta
            '''
            exist = self.get_book_meta(item)
            if not exist:
                try:
                    self.save_book_meta(item)
                except Exception as e:
                    print(item)
                    print(e)
            else:
                self.update_book_meta(item)
        elif isinstance(item, Comment):
            '''
            comment
            '''
            exist = self.get_comment(item)
            if not exist:
                try:
                    self.save_comment(item)
                except Exception as e:
                    print(item)
                    print(e)
        elif isinstance(item, PersonMeta):
            '''
            person
            '''
            exist = self.get_person_meta(item)
            if not exist:
                try:
                    self.save_person_meta(item)
                except Exception as e:
                    print(item)
                    print(e)
            else:
                self.update_person_meta(item)
        return item


class CoverPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        if 'meta' not in spider.name:
            return item
        info = self.spiderinfo
        requests = arg_to_iter(self.get_media_requests(item, info))
        dlist = [self._process_request(r, info) for r in requests]
        dfd = DeferredList(dlist, consumeErrors=1)
        return dfd.addCallback(self.item_completed, item, info)

    def file_path(self, request, response=None, info=None):
        # start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        # end of deprecation warning block

        image_guid = hashlib.sha1(to_bytes(url)).hexdigest()
        return '%s%s/%s%s/%s.jpg' % (image_guid[9], image_guid[19], image_guid[29], image_guid[39], image_guid)

    def get_media_requests(self, item, info):
        if item['cover']:
            return Request(item['cover'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if image_paths:
            item['cover'] = image_paths[0]
        else:
            item['cover'] = ''
        return item
