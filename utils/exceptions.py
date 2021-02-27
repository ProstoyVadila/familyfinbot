from controllers.finance.download_data import FILE_FORMATS


class FileFormatError(Exception):
    def __init__(self, file_format: str, message="This format isn't supported."):
        self.file_format = file_format
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.file_format} -> {self.message} It must be one of {FILE_FORMATS}'
