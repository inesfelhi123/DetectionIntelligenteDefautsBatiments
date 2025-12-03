# conversion image, encodage, logging
import tempfile
def bytes_to_file(image_bytes, suffix=".jpg"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(image_bytes)
        return tmp.name
