import os
from pathlib import Path
from main import duplicates_by_size

# def test_duplicates_by_size(tmp_path, capsys):
#     base=Path(__file__).parent
#     filepath = os.path.join(base)
#     os.makedirs('tem_path/a/b/c/d')
#     f1 = tmp_path / "a.txt"
#     f1.write_text("aaaa")
#     f2 = tmp_path / "b.txt"
#     f2.write_text("aaaa") #
#     f3 = tmp_path / "c.txt"
#     f3.write_text("bbbbb")
#
#     duplicates_by_size(str(tmp_path))
#     captured = capsys.readouterr()
#     output = captured.out
#
#     assert "a.txt" in output
#     assert "b.txt" in output
#     assert "c.txt" not in output


def path_file(dir_path):
    for py_file in Path(dir_path).glob('*'):
        print(py_file)