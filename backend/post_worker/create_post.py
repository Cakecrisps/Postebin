async def create_file_in_directory(directory, file_name, content):
    file_path = directory + file_name
    with open(file_path, 'w') as file:
        file.write(content)
