# Memory profiling with Scalene

## Prerequisites
 - Scalene does not work on Windows, but works on WSL.

## Installation

### In WSL, get this project to work:

I needed to remove and re-create the virtual environment to get it to work (using Poetry version 1.6.1).

```bash
$ poetry env list
fm-data-api-S-xerOnK-py3.11 (Activated)

$ poetry env remove fm-data-api-S-xerOnK-py3.11

$ which python3.11
/usr/bin/python3.11

$ export PYTHONPATH=/usr/bin/python3.11
$ poetry env use /usr/bin/python3.11

$ poetry install

# Test that the test script works
$ poetry run python charset_normalizer/memory_profile_test.py
```

### Install Scalene

Install Scalene in the virtual environment in the development group.

```bash
$ poetry add scalene -D
```

## Run scalene

Run your program with scalene. When you are satisfied abort (Ctrl-C) and look at the profile.html file.

```bash
$ poetry run scalene charset_normalizer/memory_profile_test.py
^C
```

Result in profile.html

