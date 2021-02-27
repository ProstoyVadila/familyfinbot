

class FileFormatError(Exception):
    def __init__(self, file_format: str, message="This format isn't supported."):
        self.file_format = file_format
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.file_format} -> {self.message}'
