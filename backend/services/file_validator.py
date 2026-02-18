# This file will handle checking the file type is valid (state needs to be managed)
from fastapi import UploadFile
from fastapi.exceptions import HTTPException

# Might need to make a constant variable for accepted files


class FileValidator:
    def __init__(self, max_size_mb: int = 50) -> None:
        # file size max
        self.max_size_mb = max_size_mb * 1024 * 1024
        # different file types that I accept (I'll add in more code files after working MVP)
        self.accepted_files = {
            "application/pdf": [".pdf"],
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [
                ".docx"
            ],
            "text/plain": [".txt", ".py", ".js", ".html", ".css", ".md"],
            "text/x-python": [".py"],
            "application/json": [".json"],
        }

    # validate the whole file
    async def validate_file(self, file: UploadFile):
        # check if file name exists
        if not file.filename:
            raise HTTPException(status_code=415, detail="File name missing")

        # check if file size is accepted
        await self.check_file_size(file)

        # check if file type is accepted
        await self.check_file_type(file)

        return True

    # check the file size
    async def check_file_size(self, file: UploadFile):
        # help with server load and memery management
        size = 0

        # reads 10mb at a time to help with handling file reading
        while chunk := await file.read(1024 * 1024 * 10):
            size += len(chunk)

            # check the size of the file
            if size > self.max_size_mb:
                raise HTTPException(
                    status_code=413, detail="File is too large to process"
                )
        # reset the pointer for reading the next file
        await file.seek(0)

        # return all good
        return True

    # check to make sure the file type is supported
    def check_file_type(self, file: UploadFile):
        # make sure that the content type is accepted
        if file.content_type not in self.accepted_files:
            raise HTTPException(status_code=415, detail="Unsupported file type")

        return True
