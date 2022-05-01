from src import annot_checking
import pytest
import os


def test_fetch_all_python_files_from_dir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    current_dir_py_files = annot_checking.fetch_all_python_files_from_dir(current_dir)
    current_dir_py_files_with_init = [
        elem for elem in current_dir_py_files if "__init__" in elem
    ]

    assert len(current_dir_py_files) == 1
    assert len(current_dir_py_files_with_init) == 0


def test_fetch_all_python_files_from_dir_with_incorrect_input():
    with pytest.raises(TypeError):
        _ = annot_checking.fetch_all_python_files_from_dir(2)
        _ = annot_checking.fetch_all_python_files_from_dir(2.4)
        _ = annot_checking.fetch_all_python_files_from_dir()
