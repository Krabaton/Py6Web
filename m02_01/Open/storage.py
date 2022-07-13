import json
import yaml


class JsonStorage:
    def __init__(self, file):
        self.file = file

    def get_value(self, key) -> str:
        with open(self.file, 'r') as f:
            data = json.load(f)
            return data.get(key, None)


class YamlStorage:
    def __init__(self, file):
        self.file = file

    def get_value(self, key) -> str:
        with open(self.file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data.get(key, None)


class StorageService:
    def __init__(self, storage: JsonStorage | YamlStorage):
        self.storage = storage

    def get(self, key: str) -> str:
        return self.storage.get_value(key)


storage_prod = StorageService(YamlStorage('data.yaml'))
print(storage_prod.get('username'), storage_prod.get('password'))


storage_stage = StorageService(JsonStorage('data.json'))
print(storage_stage.get('username'), storage_stage.get('password'))
