#encoding: utf-8
from misc.store import doubanDB


import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('movie.jl', 'w+')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class MoviePipeline(object):
    def process_item(self, item, spider):
        if spider.name != "movie":  return item
        if item.get("subject_id", None) is None: return item

        spec = { "subject_id": item["subject_id"] }
        doubanDB.movie.update(spec, {'$set': dict(item)}, upsert=True)

        return None
