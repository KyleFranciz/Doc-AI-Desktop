# This file will handle checking the file type is valid (state might need to be managed)


# validate and make sure file is good to be parsed
from typing import List

from fastapi import UploadFile


class FileValidator:
    def __init__(self, max_size_mb: int = 50, accepted_files: List[str] = None) -> None:
        self.max_size_mb = max_size_mb
        self.accepted_files = accepted_files

    pass

    # async to handle check the file
    async def validate_file(self, file: UploadFile):
        pass

    # check the file type and handle the logic
    def check_file_size(self, file: UploadFile):
        pass

    # check to make sure the file type is supported
    def check_file_type(self, file: UploadFile):
        pass
