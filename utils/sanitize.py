def sanitize_bytes(data):
    return data.replace(b'\x00', b'')
