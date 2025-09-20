0. Basic dictionary  <br>

Create a class BasicCache that inherits from BaseCaching and is a caching system:  <br>

-You must use self.cache_data - dictionary from the parent class BaseCaching  <br>
-This caching system doesn’t have limit  <br>
-def put(self, key, item):  <br>
    -Must assign to the dictionary self.cache_data the item value for the key key.  <br>
    -If key or item is None, this method should not do anything.  <br>
-def get(self, key):  <br>
    -Must return the value in self.cache_data linked to key.  <br>
    -If key is None or if the key doesn’t exist in self.cache_data, return None.  <br>

---
1. FIFO caching  <br>

Create a class FIFOCache that inherits from BaseCaching and is a caching system:  <br>

-You must use self.cache_data - dictionary from the parent class BaseCaching  <br>
-You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()   <br>
-def put(self, key, item):  <br>
    -Must assign to the dictionary self.cache_data the item value for the key key.  <br>
    -If key or item is None, this method should not do anything.  <br>
    -If the number of items in self.cache_data is higher that 
     BaseCaching.MAX_ITEMS:  <br>
        -you must discard the first item put in cache (FIFO algorithm)  <br>
        -you must print DISCARD: with the key discarded and following by a new line  <br>
-def get(self, key):  <br>
    -Must return the value in self.cache_data linked to key.  <br>
    -If key is None or if the key doesn’t exist in self.cache_data, return None.  <br>

---
2. LIFO Caching  <br>

Create a class LIFOCache that inherits from BaseCaching and is a caching system:  <br>

    -You must use self.cache_data - dictionary from the parent class BaseCaching  <br>
    -You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()  <br>
    -def put(self, key, item):  <br>
        -Must assign to the dictionary self.cache_data the item value for the key key.  <br>
        -If key or item is None, this method should not do anything.  <br>
        -If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:  <br>
            -you must discard the last item put in cache (LIFO algorithm)  <br>
            -you must print DISCARD: with the key discarded and following by a new line  <br>
    -def get(self, key):  <br>
        -Must return the value in self.cache_data linked to key.  <br>
        -If key is None or if the key doesn’t exist in self.cache_data, return None.  <br>

---
3. LRU Caching  <br>

Create a class LRUCache that inherits from BaseCaching and is a caching system:  <br>

-You must use self.cache_data - dictionary from the parent class BaseCaching  <br>
-You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()  <br>
-def put(self, key, item):  <br>
    -Must assign to the dictionary self.cache_data the item value for the key key.  <br>
    -If key or item is None, this method should not do anything.  <br>
    -If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:  <br>
        -you must discard the least recently used item (LRU algorithm)  <br>
        -you must print DISCARD: with the key discarded and following by a new line  <br>
-def get(self, key):  <br>
    -Must return the value in self.cache_data linked to key.  <br>
    -If key is None or if the key doesn’t exist in self.cache_data, return None.  <br>

---
4. MRU Caching  <br>

Create a class MRUCache that inherits from BaseCaching and is a caching system:  <br>

-You must use self.cache_data - dictionary from the parent class BaseCaching  <br>
-You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()  <br>
-def put(self, key, item):  <br>
    -Must assign to the dictionary self.cache_data the item value for the key key.  <br>
    -If key or item is None, this method should not do anything.  <br>
    -If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:  <br>
        -you must discard the most recently used item (MRU algorithm)  <br>
        -you must print DISCARD: with the key discarded and following by a new line  <br>
-def get(self, key):  <br>
    -Must return the value in self.cache_data linked to key.  <br>
    -If key is None or if the key doesn’t exist in self.cache_data, return None.  <br>

    
