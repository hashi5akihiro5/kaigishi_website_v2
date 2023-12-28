EXAMTYPE = (
    ('writing', '筆記'),
    ('speaking', '口述'),
)

NAVIGATION_OR_MECHANISM = (
    ('navigation', '航海'),
    ('mechanism', '機関'),
)

GRADE = (
    ('grade1', '1級'),
    ('grade2', '2級'),
    ('grade3', '3級'),
)

SUBJECT_CHOICES = {
    'navigation': 1,
    'operation': 2,
    'law': 3,
    'english': 4,
    'mechanism1': 5,
    'mechanism2': 6,
    'mechanism3': 7,
    'working': 8,
}

SUBJECT = (
    ('navigation', '航海'),
    ('operation', '運用'),
    ('law', '法規'),
    ('english', '英語'),
    ('mechanism1', '機関1'),
    ('mechanism2', '機関2'),
    ('mechanism3', '機関3'),
    ('working', '執務一般'),
)

SHOMON = (
    (1, '一'),
    (2, '二'),
    (3, '三'),
    (4, '四'),
    (5, '五'),
)