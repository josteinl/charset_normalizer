
"""
   poetry run python3 -m scalene charset_normalizer/memory_profile_test.py
"""

import sys
# from charset_normalizer import detect, from_bytes, from_fp
from charset_normalizer.api import from_bytes

file_name = "data/memory_profile_test.txt"

# with open(file_name, "rb") as file:
#     data = file.read()
#     result = detect(data)
#     print(f"{sys.getsizeof(result)=}")
#     print(f"{result=}")


with open(file_name, "rb") as file:
    data = file.read()
    result = from_bytes(data)
    # print(f"{sys.getsizeof(result._results)=}")
    for r in result._results:
        print(f"{sys.getsizeof(r)=}")
        print(f"{sys.getsizeof(r.raw)=}")
        print(f"{id(r.raw)=}")
    best = result.best()
    print(f"{best=}")


# with open(file_name, "rb") as file:
#     result = from_fp(file)
#     print(f"{sys.getsizeof(result)=}")
#     best = result.best()
#     print(f"{best=}")
