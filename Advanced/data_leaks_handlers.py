def create_leak():
    # File is opened but never explicitly closed
    file = open("my_data.txt", "w")
    file.write("Some data")
    # No file.close() call here, leading to a potential leak

def prevent_leak():
    with open("my_data.txt", "w") as file:
        file.write("Some data")
    # The 'with' statement ensures the file is closed automatically
