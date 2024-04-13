import redis

class DistributedStorage:
    def __init__(self, nodes):
        self.nodes = nodes
        self.redis_connections = [redis.StrictRedis(node[0], node[1]) for node in nodes]

    def set(self, key, value):
        """
        Set a key-value pair in the distributed storage.
        """
        node_index = hash(key) % len(self.nodes)
        redis_connection = self.redis_connections[node_index]
        redis_connection.set(key, value)

    def get(self, key):
        """
        Retrieve the value associated with the given key from the distributed storage.
        """
        node_index = hash(key) % len(self.nodes)
        redis_connection = self.redis_connections[node_index]
        return redis_connection.get(key)

# Example usage:
if __name__ == "__main__":
    # Define nodes (host, port) for distributed storage
    nodes = [("localhost", 6379), ("localhost", 6380), ("localhost", 6381)]

    # Initialize distributed storage
    distributed_storage = DistributedStorage(nodes)

    # Set key-value pairs
    distributed_storage.set("key1", "value1")
    distributed_storage.set("key2", "value2")

    # Retrieve values
    value1 = distributed_storage.get("key1")
    value2 = distributed_storage.get("key2")

    print("Value for key1:", value1)
    print("Value for key2:", value2)
