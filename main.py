class MemoryBlock:
    def __init__(self, size, allocated=False):
        self.size = size
        self.allocated = allocated
 
class NextFitMemoryAllocator:
    def __init__(self, predefined_blocks):
        self.memory_blocks = [MemoryBlock(size) for size in predefined_blocks]
        self.last_allocated_index = 0  # Tracks the last allocated position
 
    def allocate(self, request_size):
        block_count = len(self.memory_blocks)
        start_index = self.last_allocated_index
 
        for _ in range(block_count):
            block = self.memory_blocks[self.last_allocated_index]
            if not block.allocated and block.size >= request_size:
                if block.size > request_size:
                    self.memory_blocks.insert(self.last_allocated_index + 1, MemoryBlock(block.size - request_size))
                    block.size = request_size
                block.allocated = True
                print(f"Allocated {request_size} KB at block {self.last_allocated_index + 1}.")
                return True
            self.last_allocated_index = (self.last_allocated_index + 1) % block_count
 
        print(f"Failed to allocate {request_size} KB. Not enough space.")
        return False
 
    def display_memory(self):
        print("Memory State:")
        for i, block in enumerate(self.memory_blocks):
            status = "Allocated" if block.allocated else "Free"
            print(f"Block {i + 1}: {block.size} KB ({status})")
 
if __name__ == "__main__":
    predefined_blocks = [200, 300, 100, 500]
    allocator = NextFitMemoryAllocator(predefined_blocks)
 
    print("Initial Memory State:")
    allocator.display_memory()
 
    while True:
        request = input("Enter memory request size (in KB) or 'exit' to quit: ").lower()
        if request == 'exit':
            break
        if request.isdigit():
            allocator.allocate(int(request))
            allocator.display_memory()
        else:
            print("Please enter a valid integer.")
 
    print("\nFinal Memory State:")
    allocator.display_memory()
