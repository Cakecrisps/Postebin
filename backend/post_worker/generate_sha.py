import hashlib
import hashlib
import random
import string

async def generate_random_hash(length):
    characters = string.ascii_letters + string.digits
    random_data = ''.join(random.choice(characters) for _ in range(length))
    random_hash = hashlib.sha256(random_data.encode()).hexdigest()[:length]
    return random_hash

