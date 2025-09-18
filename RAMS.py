class VirtualRAM:
    def __init__(self):
        self.stack = []
        self.heap = {}
        self.data_segment = {}
        self.code_segment = []

    # Stack operations
    def push_stack(self, value):
        self.stack.append(value)

    def pop_stack(self):
        return self.stack.pop() if self.stack else None

    # Heap operations
    def allocate_heap(self, var_name, value):
        self.heap[var_name] = value
    def free_heap(self, var_name):
        if var_name in self.heap:
            del self.heap[var_name]

    # Data segment
    def define_global(self, var_name, value):
        self.data_segment[var_name] = value

    # Code segment
    def load_instruction(self, instruction):
        self.code_segment.append(instruction)

    # Debug view
    def show_memory(self):
        print("=== Virtual RAM ===")
        print("Stack:", self.stack)
        print("Heap:", self.heap)
        print("Data Segment:", self.data_segment)
        print("Code Segment:", self.code_segment)
        print("===================")


# Esempio d'uso
ram = VirtualRAM()
ram.push_stack("return_address")
ram.allocate_heap("obj1", {"x": 10, "y": 20})
ram.define_global("counter", 0)
ram.load_instruction("MOV A, B")
ram.show_memory()
