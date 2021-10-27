import io
import json
import random


class DataBase:
    data = []
    file = None

    def __init__(self):
        self.file = open('data.json', )
        self.data = json.load(self.file)

    def get_all(self):
        return self.data

    def get(self, id):
        return next((item for item in self.data if item['id'] == id), None)

    def add(self, text):
        if any((item for item in self.data if item['text'] == text)):
            raise Exception('Item has been existed')
        item = {
            'id': random.randrange(1000000000),
            'text': text,
            'status': False
        }
        self.data.append(item)
        self.write_data()
        return item

    def update(self, task, id):
        self.data = [task if item['id'] == id else item for item in self.data]
        self.write_data()

    # update status
    def update_field(self, field, value, id):
        item = self.get(id)
        item[field] = value
        print(item)
        self.update(item, id)

    def delete(self, ID):
        self.data = [item for item in self.data if item['id'] != ID]
        self.write_data()

    def write_data(self):
        with io.open('data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.data, ensure_ascii=False))
