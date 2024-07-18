import os

async def check_file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        return True
    else:
        return False
