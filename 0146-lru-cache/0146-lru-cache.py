import collections

class LRUCache:

    def __init__(self, capacity: int):
        self._data = collections.OrderedDict()
        self._size = capacity
    
    def _update_key(self, key):
        result = self._data[key]
        del self._data[key]
        self._data[key] = result
        
    def get(self, key: int) -> int:
        if key not in self._data.keys():
            return -1
        self._update_key(key)
        return self._data[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self._data.keys():
            self._update_key(key)
            self._data[key] = value
            return
        
        if len(self._data) < self._size:
            self._data[key] = value
            return
        
        least_used_key = list(self._data)[0]
        del self._data[least_used_key]
        self._data[key] = value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)