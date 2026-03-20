# cheerfully-sober
This is  a playfull app which can be usef for having a good drink 
The standard scientific approach uses Widmark’s formula:
BAC = (A/(r.w) ).100 − (β⋅t)
Where:


A = total grams of alcohol consumed
r = body water constant (≈ 0.68 men, 0.55 women)
W = body weight in grams
β = elimination rate per hour (≈ 0.015 % BAC/hour)
t = hours since first drink

Grams of alcohol per drink:
grams=volume (ml)×ABV (%)×0.789
0.789 = density of ethanol in g/ml

⚠️ Important: This gives an estimate of BAC, not a “number of shots to blackout” — for safety, you should always present it as a risk/impairment estimate.
## Features

### Profile Management
Save, load, and delete user profiles for quick calculations:
- **Save Profile**: Store your personal information (weight, height, age, sex, and unit preference)
- **Load Profile**: Quickly load a saved profile to avoid re-entering your data
- **Delete Profile**: Remove profiles you no longer need

Profiles are stored locally in your home directory at `~/.cheerfully_sober_profiles.json`
