# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import sys
import tempfile
from pathlib import Path

import pytest

tests_dir = Path(__file__).resolve().parent
test_file_dir = tests_dir / 'test_files'
root_dir = tests_dir.parent

sys.path.append(str(root_dir))

from extract_office_text import ExtractExcel

excel_extracter = ExtractExcel()


def test_with_images():
    excel_path = test_file_dir / 'excel_with_image.xlsx'
    with tempfile.TemporaryDirectory() as tmp_dir:
        res = excel_extracter(excel_path, is_save_img=True,
                              save_img_dir=tmp_dir)

        img_list = list(Path(tmp_dir).glob('*.*'))
        assert len(img_list) == 2
        assert img_list[0].name == 'image1.jpeg'
        assert res[0][:9] == '|    | 班级'


def test_without_images():
    excel_path = test_file_dir / 'excel_example.xlsx'
    with tempfile.TemporaryDirectory() as tmp_dir:
        with pytest.warns(UserWarning,
                          match='does not contain any images.'):
            res = excel_extracter(excel_path,
                                  is_save_img=True,
                                  save_img_dir=tmp_dir)