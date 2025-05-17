from linked_list import Node, LinkedList

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for item in range(array_size)]  # List of LinkedLists

    def hash(self, key):
        key_bytes = key.encode()  # Convert key to bytes
        hash_code = sum(key_bytes)  # Sum up the character encodings
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size  # Ensures the index is within bounds of the array

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])  # Create a new node with the key-value pair
        list_at_array = self.array[array_index]
        
        # Iterate over the linked list
        current_node = list_at_array.head
        while current_node:
            if current_node.value[0] == key:  # If key is found, overwrite its value
                current_node.value = [key, value]
                return
            current_node = current_node.next
        
        list_at_array.insert(payload)  # Insert the new node if key not found

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        
        # Iterate over the linked list
        current_node = list_at_index.head
        while current_node:
            if current_node.value[0] == key:
                return current_node.value[1]  # Return the value if key matches
            current_node = current_node.next
        return None  # Return None if the key is not found


from blossom_lib import flower_definitions

# Create a HashMap instance with size equal to the length of flower_definitions
blossom = HashMap(len(flower_definitions))

# Assign flower names and their meanings to the hash map
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

# Retrieve the meaning of a flower
print(blossom.retrieve('daisy'))
