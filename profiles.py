"""Profile Management Module for BAC Calculator"""

import json
import os
from pathlib import Path


# Profile storage file path
PROFILES_FILE = Path.home() / ".cheerfully_sober_profiles.json"


def load_all_profiles():
    """
    Load all saved profiles from the JSON file.
    
    Returns:
        Dictionary of profiles {profile_name: profile_data}
    """
    if not PROFILES_FILE.exists():
        return {}
    
    try:
        with open(PROFILES_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def save_profile(profile_name, weight, height, age, sex, unit_system):
    """
    Save a user profile.
    
    Args:
        profile_name: Name of the profile
        weight: Weight value (in current unit system)
        height: Height value (in current unit system)
        age: Age in years
        sex: Biological sex ("male" or "female")
        unit_system: Unit system ("metric" or "imperial")
        
    Returns:
        True if successful, False otherwise
    """
    if not profile_name or not profile_name.strip():
        return False
    
    profiles = load_all_profiles()
    
    profile_data = {
        "weight": weight,
        "height": height,
        "age": age,
        "sex": sex,
        "unit_system": unit_system
    }
    
    profiles[profile_name.strip()] = profile_data
    
    try:
        with open(PROFILES_FILE, 'w') as f:
            json.dump(profiles, f, indent=2)
        return True
    except IOError:
        return False


def load_profile(profile_name):
    """
    Load a specific profile by name.
    
    Args:
        profile_name: Name of the profile to load
        
    Returns:
        Profile data dictionary or None if not found
    """
    profiles = load_all_profiles()
    return profiles.get(profile_name)


def delete_profile(profile_name):
    """
    Delete a profile by name.
    
    Args:
        profile_name: Name of the profile to delete
        
    Returns:
        True if successful, False otherwise
    """
    profiles = load_all_profiles()
    
    if profile_name not in profiles:
        return False
    
    del profiles[profile_name]
    
    try:
        with open(PROFILES_FILE, 'w') as f:
            json.dump(profiles, f, indent=2)
        return True
    except IOError:
        return False


def get_profile_names():
    """
    Get a list of all saved profile names.
    
    Returns:
        List of profile names
    """
    profiles = load_all_profiles()
    return sorted(profiles.keys())
