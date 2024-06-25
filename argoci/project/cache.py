import json
import os
from datetime import datetime, timedelta


class Cache:
    def __init__(self, file_name="cache.json"):
        self.file_name = file_name
        self.load_cache()

    def load_cache(self):
        """Will load cache data or create an empty one in case it's empty"""
        if os.path.exists(self.file_name):
            print("Cache file found")
            with open(self.file_name, "r") as file:
                self.cache_data = json.load(file)
            self.clear_expired_cache()
        else:
            print("Cache file not found")
            self.cache_data = {}
        return self.cache_data

    def save_to_cache(self, location, data):
        """"will save a new data into the cache"""
        self.clear_expired_cache()
        self.cache_data[location] = {
            "data": data,
            "timestamp": datetime.now().isoformat()
        }
        with open(self.file_name, 'w') as file:
            json.dump(self.cache_data, file, indent=4)

    def clear_expired_cache(self):
        """Will go throw the file and remove cached data that's expired over 2 hours"""
        now = datetime.now()
        for location, info in list(self.cache_data.items()):
            timestamp = datetime.fromisoformat(info["timestamp"])
            if now - timestamp > timedelta(hours=2):
                del self.cache_data[location]
        with open(self.file_name, 'w') as file:
            json.dump(self.cache_data, file, indent=4)
