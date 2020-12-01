
def read_file_content(path: str) -> str:
    file = open(path, "r")
    r = file.read()
    file.close()

    return r
