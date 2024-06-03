import os
from datetime import date


def find_key_for_value(value, tuple_list):
    for key, val in tuple_list:
        if val == value:
            return key
    return None


def get_exam_id(examtype, navigation_or_engineering, grade, year, month):
    exam_id = []
    # 試験種類（1:筆記, 2:口述）
    if examtype == "writing":
        exam_id.append(1)
    else:
        exam_id.append(2)
    # 航機種類（1:航海, 2:機械）
    if navigation_or_engineering == "navigation":
        exam_id.append(1)
    else:
        exam_id.append(2)
    # 級名（1:1級, 2:２級, 3:3級）
    if grade == "grade1":
        exam_id.append(1)
    elif grade == "grade2":
        exam_id.append(2)
    else:
        exam_id.append(3)
    # 年度
    exam_id.append(year)
    # 月度
    exam_id.append(str(month).zfill(2))
    exam_id = "".join(str(i) for i in exam_id)
    return exam_id


def default_exam_id():
    today = date.today()
    exam_id = "".join(
        [
            str(1),  # 筆記口述種類（1:筆記, 2:口述）
            str(1),  # 航機種類（1:航海, 2:機関）
            str(1),  # 級名(1:1級, 2:2級, 3:3級)
            str(today.year),  # 年度
            str(today.month).zfill(2),  # 月度
        ]
    )
    return exam_id


def get_file_path(instance, filename):
    return os.path.join(
        str("PDF"),
        str(instance.exam.get_exam_type_display()),
        str(instance.exam.get_navigation_or_engineering_display()),
        str(instance.exam.get_grade_display()),
        f"{str(instance.exam.date.year)}年",
        f"{str(instance.exam.date.month)}月",
        str(instance.get_name_display()),
        filename,
    )


def get_image_upload_path(instance, filename):
    return os.path.join(
        str(instance.subject.exam.get_exam_type_display()),
        str(instance.subject.exam.get_navigation_or_engineering_display()),
        str(instance.subject.exam.get_grade_display()),
        f"{str(instance.subject.exam.date.year)}年",
        f"{str(instance.subject.exam.date.month)}月",
        str(instance.subject.get_name_display()),
        f"大問{str(instance.daimon)}",
        filename,
    )
