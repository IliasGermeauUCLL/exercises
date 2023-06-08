class StorageDevice:
    def __init__(self, block_count, block_size):
        self._available_blocks = set(range(block_count))
        self._used_blocks = set()
        self._block_size = block_size

    @property
    def available_block_count(self):
        return len(self._available_blocks)

    @property
    def used_block_count(self):
        return len(self._used_blocks)

    @property
    def total_block_count(self):
        return self.available_block_count + self.used_block_count

    @property
    def block_size(self):
        return self._block_size

    def allocate(self, block_count):
        if block_count > self.available_block_count:
            raise RuntimeError("Insufficient available blocks")
        blocks = list(self._available_blocks)[:block_count]
        self._available_blocks.difference_update(blocks)
        self._used_blocks.update(blocks)
        return blocks

    def free(self, blocks):
        if not set(blocks).issubset(self._used_blocks):
            raise RuntimeError("Cannot free blocks that are not in use")
        self._used_blocks.difference_update(blocks)
        self._available_blocks.update(blocks)


class Entity:
    def __init__(self, storage, name):
        if not Entity.is_valid_name(name):
            raise RuntimeError("Invalid name")
        self._storage = storage
        self._name = name

    @staticmethod
    def is_valid_name(name):
        if not 1 <= len(name) <= 16:
            return False
        return all(c.isalnum() or c == '.' for c in name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not Entity.is_valid_name(new_name):
            raise RuntimeError("Invalid name")
        self._name = new_name
