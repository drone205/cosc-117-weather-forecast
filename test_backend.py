from backend import calc_aqi_level
from config import AQI_INTERVALS

def test_so2_level_calculation():
    """
    Tests the case we found in the debugger.
    SO2 concentration of "77" should be level 2 ("good").
    """
    concentration = "77"
    intervals = AQI_INTERVALS["so2"]

    #We expect Level 2 (Good)
    expected_level = 2
    calculated_level = calc_aqi_level(concentration, intervals)
    assert calculated_level == expected_level

def test_co_level_calculation():
    #Tests CO level matches expected value
    concentration = "684.85"
    intervals = AQI_INTERVALS["co"]

    #we expect Leval 1 (Exellent)
    expected_level = 1
    calculated_level = calc_aqi_level(concentration, intervals)
    assert calculated_level == expected_level