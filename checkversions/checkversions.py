import os
from packaging import version
from packaging.version import InvalidVersion
from dotsetup import DotSetup, FileNotFoundError, VariableNotFoundError, JSONDecodeError

def get_default_hierarchy_from_json():
    """
    Load the default hierarchy from a JSON file.

    This function initializes a DotSetup instance, gets the absolute path to
    the 'default_hierarchy.json' file, and loads the hierarchy from the JSON file.

    Returns:
        dict: The default version hierarchy loaded from the JSON file.

    Raises:
        FileNotFoundError: If the 'default_hierarchy.json' file is not found.
        VariableNotFoundError: If a variable is not found during JSON loading.
        JSONDecodeError: If there is an error decoding JSON.
    """
    try:
        # Initialize DotSetup
        ds = DotSetup()

        # Get absolute path to JSON file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(script_dir, '../default_hierarchy.json')

        # Load from JSON file
        value_json = ds.load('default_hierarchy', file_type='json', file_path=json_file_path)
        return value_json
    except (FileNotFoundError, VariableNotFoundError, JSONDecodeError) as e:
        print(f"Error loading default hierarchy from JSON: {e}")
        return {"beta": 0, "prerelease": 1, "alpha": 2, "unstable": 3, "stable": 4, "release": 5}

def compare_versions(current_version, latest_version, custom_hierarchy=None, older_version=False):
    """
    Compare two versions and determine the latest or older version.

    This function compares two versions, taking into account version numbers,
    hyphen-separated parts, and additional words (e.g., beta, release, alpha).

    Args:
        current_version (str): The current version.
        latest_version (str): The version to compare against.
        custom_hierarchy (dict, optional): Custom version hierarchy. Defaults to None.
        older_version (bool, optional): If True, return the older version. Defaults to False.

    Returns:
        str: The latest or older version, considering version numbers and hierarchy.

    Raises:
        InvalidVersion: If there is an issue with the version comparison.
    """
    try:
        # Check if 'v' prefix is present and retain it in the output
        current_version_output = current_version if current_version.startswith('v') else 'v' + current_version
        latest_version_output = latest_version if latest_version.startswith('v') else 'v' + latest_version

        # Extract version codes before hyphen
        current_version_before_hyphen = current_version.split('-')[0]
        latest_version_before_hyphen = latest_version.split('-')[0]

        # Extract additional words (e.g., beta, release, alpha, stable, unstable)
        current_version_words = ''.join(filter(str.isalpha, current_version))
        latest_version_words = ''.join(filter(str.isalpha, latest_version))

        # Extract parts after hyphen for additional comparison
        current_version_after_hyphen_parts = current_version.split('-')[1:] if '-' in current_version else []
        latest_version_after_hyphen_parts = latest_version.split('-')[1:] if '-' in latest_version else []

        # Check if after hyphen contains a word not available in default or custom hierarchy
        current_version_after_hyphen_word = ''.join(filter(str.isalpha, current_version_after_hyphen_parts[0])) if current_version_after_hyphen_parts else ''
        latest_version_after_hyphen_word = ''.join(filter(str.isalpha, latest_version_after_hyphen_parts[0])) if latest_version_after_hyphen_parts else ''

        # Default version hierarchy
        default_hierarchy = get_default_hierarchy_from_json()

        # Use custom hierarchy if provided, otherwise use default
        version_hierarchy = custom_hierarchy or default_hierarchy

        # Check if the word after hyphen is in the hierarchy, else raise an error
        if current_version_after_hyphen_word and current_version_after_hyphen_word not in version_hierarchy:
            raise InvalidVersion(f"Version hierarchy not found for '{current_version_after_hyphen_word}'. Use custom hierarchy.")
        if latest_version_after_hyphen_word and latest_version_after_hyphen_word not in version_hierarchy:
            raise InvalidVersion(f"Version hierarchy not found for '{latest_version_after_hyphen_word}'. Use custom hierarchy.")

        # Use packaging.version for version comparison
        current_version_obj = version.parse(current_version_before_hyphen)
        latest_version_obj = version.parse(latest_version_before_hyphen)

        # Compare version numbers first
        if current_version_obj < latest_version_obj:
            return current_version_output if older_version else latest_version_output
        elif current_version_obj > latest_version_obj:
            return latest_version_output if older_version else current_version_output

        # Compare hierarchy only if version numbers are equal
        if version_hierarchy.get(current_version_after_hyphen_word, 5) < version_hierarchy.get(latest_version_after_hyphen_word, 5):
            return current_version_output if older_version else latest_version_output
        elif version_hierarchy.get(current_version_after_hyphen_word, 5) > version_hierarchy.get(latest_version_after_hyphen_word, 5):
            return latest_version_output if older_version else current_version_output
        elif version_hierarchy.get(current_version_words, 5) < version_hierarchy.get(latest_version_words, 5):
            return current_version_output if older_version else latest_version_output
        elif version_hierarchy.get(current_version_words, 5) > version_hierarchy.get(latest_version_words, 5):
            return latest_version_output if older_version else current_version_output

        return current_version_output

    except InvalidVersion as e:
        return f"Error: {e}"
