def find_key_for_value(value, tuple_list):
    for key, val in tuple_list:
        if val == value:
            return key
    return None


def get_exam_id(examtype, navigation_or_mechanism, grade, year, month):
    exam_id = []
    # 試験種類（1:筆記, 2:口述）
    if examtype == 'writing':
        exam_id.append(1)
    else:
        exam_id.append(2)
    # 航機種類（1:航海, 2:機械）
    if navigation_or_mechanism == 'navigation':
        exam_id.append(1)
    else:
        exam_id.append(2)
    # 級名（1:1級, 2:２級, 3:3級）
    if grade == 'grade1':
        exam_id.append(1)
    elif grade == 'grade2':
        exam_id.append(2)
    else:
        exam_id.append(3)
    # 年度
    exam_id.append(year)
    # 月度
    exam_id.append(str(month).zfill(2))
    exam_id = ''.join(str(i) for i in exam_id)
    return exam_id