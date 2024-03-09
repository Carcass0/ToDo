from os import path

def resource_path(relative_path:str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)