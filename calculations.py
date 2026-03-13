"""BAC Calculation Module"""

from constants import (
    R_MAN,
    R_WOMAN,
    ETHANOL_DENSITY_G_ML,
    ELIMINATION_RATE_PER_HR,
    BAC_LEVELS
)


def calculate_alcohol_grams(volume_ml, abv_percent):
    """
    Calculate grams of alcohol in a drink.
    
    Args:
        volume_ml: Volume of drink in milliliters
        abv_percent: Alcohol by volume percentage
        
    Returns:
        Grams of alcohol
    """
    return volume_ml * (abv_percent / 100) * ETHANOL_DENSITY_G_ML


def get_widmark_factor(sex):
    """
    Get the Widmark factor based on biological sex.
    
    Args:
        sex: Sex identifier ("male" or "female")
        
    Returns:
        Widmark factor (r value)
    """
    if sex.lower() == "male":
        return R_MAN
    else:
        return R_WOMAN


def calculate_bac(weight_kg, sex, alcohol_grams, hours_elapsed):
    """
    Calculate Blood Alcohol Content using Widmark formula.
    
    Args:
        weight_kg: Body weight in kilograms
        sex: Biological sex ("male" or "female")
        alcohol_grams: Grams of pure alcohol consumed
        hours_elapsed: Hours since first drink
        
    Returns:
        BAC as a percentage (e.g., 0.08 for 0.08%)
    """
    r = get_widmark_factor(sex)
    weight_g = weight_kg * 1000
    
    # Widmark formula
    bac = (alcohol_grams / (weight_g * r)) * 100
    
    # Account for alcohol elimination over time
    bac -= ELIMINATION_RATE_PER_HR * hours_elapsed
    
    # BAC cannot be negative
    return max(bac, 0.0)


def get_bac_description_and_color(bac):
    """
    Get description and color code for a given BAC level.
    
    Args:
        bac: Blood Alcohol Content percentage
        
    Returns:
        Tuple of (description, color_code)
    """
    for threshold, description, color in BAC_LEVELS:
        if bac < threshold:
            return description, color
    
    # Fallback (shouldn't reach here due to inf in BAC_LEVELS)
    return BAC_LEVELS[-1][1], BAC_LEVELS[-1][2]
