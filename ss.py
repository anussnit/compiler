text = "Hello, this is a sample text for testing the seek function."

# Writing the sample text to a file
with open("example.txt", "w") as file:
    file.write(text)

# Reading the file and using seek() with different whence values
with open("example.txt", "rb") as file:
    # whence=0: Seek from the beginning of the file
    file.seek(7, 0)  # Move to the 7th byte from the start
    print("whence=0, offset=7:", file.read(5).decode())  # Output: "this"

    # whence=1: Seek from the current position
    file.seek(5, 1)  # Move forward 5 bytes from the current position
    print("whence=1, offset=5:", file.read(4).decode())  # Output: " is"

    # whence=2: Seek from the end of the file
    file.seek(-8, 2)  # Move backward 8 bytes from the end of the file
    print("whence=2, offset=-8:", file.read(8).decode())  # Output: "unction."