# import pandas as pd
#
# students = [1, 2, None]
# results = pd.Series(students)
#
# print(results)


import numpy as np
import pandas as pd

students = [
    ('Alice', 'Brown'),
    ('Jack', 'White'),
    ('Molly', 'Green')
]

printer = pd.Series(students)

print(printer)


