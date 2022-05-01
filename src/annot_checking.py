import os


def fetch_all_python_files_from_dir(directory: str) -> list[str]:
    """
    Fetch all python files (.py) recursively from a given directory
    omitting __init__.py files

    Args:
        directory (str): directory from which files should be searched

    Returns:
        list[str]: list of python files
    """
    res: list[str] = []
    for root, _, files in os.walk(directory, topdown=False):
        for name in files:
            if (not name.endswith(".py")) or name.startswith("__init__"):
                continue
            res.append(os.path.join(root, name))
    return res


if __name__ == "__main__":
    fetch_all_python_files_from_dir("..")
