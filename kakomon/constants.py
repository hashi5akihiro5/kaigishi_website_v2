EXAMTYPE = (
    ("writing", "筆記"),
    ("speaking", "口述"),
)

NAVIGATION_OR_ENGINEERING = (
    ("navigation", "航海"),
    ("engineering", "機関"),
)

GRADE = (
    ("grade1", "1級"),
    ("grade2", "2級"),
    ("grade3", "3級"),
)

SUBJECT_CHOICES = {
    "navigation": 1,
    "operation": 2,
    "law": 3,
    "english": 4,
    "engineering1": 5,
    "engineering2": 6,
    "engineering3": 7,
    "working": 8,
}

SUBJECT = (
    ("navigation", "航海"),
    ("operation", "運用"),
    ("law", "法規"),
    ("english", "英語"),
    ("engineering1", "機関1"),
    ("engineering2", "機関2"),
    ("engineering3", "機関3"),
    ("working", "執務一般"),
)

SHOMON = (
    (1, "一"),
    (2, "二"),
    (3, "三"),
    (4, "四"),
    (5, "五"),
)

IMG_DESCRIPTION_OR_QUESTION = (
    ("description", "説明"),
    ("question", "問題"),
)

IMG_RIGHT_OR_UNDER = (
    ("right", "右"),
    ("under", "下"),
)
