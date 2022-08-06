# Hashtables
A Hash Table is a data structure that stores data in an associative manner.

## Challenge
Implement a Hashtable Class with the following methods:
- set

Arguments: key, value

Returns: nothing

- get

Arguments: key

Returns: Value associated with that key in the table

- contains

Arguments: key

Returns: Boolean, indicating if the key exists in the table already.

- keys

Returns: Collection of keys

- hash

Arguments: key

Returns: Index in the collection for that key

## Approach & Efficiency
Time Complexity: O(1)
Space Complexity: O(n)
## API
- hash(key) : it hashing any inputed key with hash method and returns Index in the collection for that key

- set(key, value) : it used to add the key and value to the hash_table.

- get(key) : it used to get  the value of inputed key if it exist in the hash table

- contains(key) : to make sure if the key is exist on hash table, this fuction will check and return boolean
- keys() : return Collection of keys