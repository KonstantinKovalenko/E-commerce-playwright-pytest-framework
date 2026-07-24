import uuid

def generate_email():
    return f"qa_{uuid.uuid4().hex[:8]}@example.com"