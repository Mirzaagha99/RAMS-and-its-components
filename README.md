# RAMS-and-its-components
Random Access Memory (RAM) is a type of computer memory that stores data temporarily. When you turn off your computer, the data in RAM disappears, unlike the data on your hard drive, which stays saved. RAM helps your computer run programs and process information faster. This is similar to how the brain’s memory helps us remember things.
RAMS is composed by the following elements:
<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/7debd3cd-3007-40df-a05b-90a7b96937cf" />


1. Stack

🔹 Purpose:

  Used for function calls, local variables, and return addresses.

🔹 Logic:

  •	Operates as a LIFO (Last In, First Out) structure.

  •	Every time a function is called, a stack frame is created containing: 

    o	Function parameters

    o	Local variables

    o	Return address

  •	When the function ends, the frame is popped off the stack.
________________________________________

2. Heap

  🔹 Purpose:

    Stores dynamically allocated memory, useful for data that needs to persist beyond a function's scope.

  🔹 Logic:

    •	Managed manually (malloc, new, free, delete) or automatically (garbage collection).

    •	No fixed structure; grows as needed.

    •	Slower than stack but more flexible.

    •	Ideal for objects, arrays, and complex data structures.
________________________________________
3. Data Segment

🔹 Purpose:

  Holds global and static variables.

🔹 Logic:

    •	Divided into: 

      o	Initialized Data Segment: variables with initial values.

      o	Uninitialized Data Segment (BSS): variables without initial values.

    •	Allocated when the program starts and persists until it ends.

________________________________________

4. Code Segment (Text Segment)

🔹 Purpose:

    Contains the executable instructions of the program.

🔹 Logic:

    •	Read-only to prevent accidental modification.

    •	Includes compiled machine code that the CPU executes.

________________________________________

5. Memory-Mapped I/O / Shared Memory

🔹 Purpose:

    Used for hardware communication or inter-process communication.

🔹 Logic:

    •	Some RAM areas are mapped to hardware registers.

    •	Shared memory allows multiple processes to access the same data.

