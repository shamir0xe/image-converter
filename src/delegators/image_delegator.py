from __future__ import annotations
import pillow_avif
from PIL import Image


class ImageDelegator:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_file(self) -> ImageDelegator:
        self.image = Image.open(self.file_path)
        return self
    
    def save_file(self, path: str, file_format: str) -> ImageDelegator:
        self.image.save(path + '.' + file_format)
        return self
