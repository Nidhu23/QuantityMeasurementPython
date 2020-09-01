from com.quantitymeasurement.src.QuantityMeasurement import Feet


def test_givenZeroFtAndZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0)
    second_feet = Feet(0)
    assert first_feet == second_feet
