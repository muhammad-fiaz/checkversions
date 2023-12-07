"""
CheckVersions Package

This package provides functionality for comparing version numbers and determining the latest version
based on a specified hierarchy.

Usage:
    from checkversions import *

    current_version = "v1.0.0"
    latest_version = "v1.0.0-beta"
    result = compare_versions(current_version, latest_version)
    print(result)

Functions:
    - compare_versions(current_version, latest_version, custom_hierarchy=None):
        Compares two versions and returns the latest version based on the provided hierarchy.

    - get_default_hierarchy_from_json():
        Loads the default hierarchy from a JSON file and returns it as a dictionary.

Modules:
    - checkversions.py
        Contains the implementation of version comparison functions.

    - default_hierarchy.json
        Default hierarchy configuration file in JSON format.

Exceptions:
    - DotSetupException
    - FileNotFoundError
    - VariableNotFoundError
    - JSONDecodeError

Note: Ensure that 'dotsetup' and 'packaging' packages are installed for proper functionality.
"""

from .checkversions import compare_versions
