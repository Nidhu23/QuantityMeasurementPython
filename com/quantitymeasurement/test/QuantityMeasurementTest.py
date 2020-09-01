from com.quantitymeasurement.src.QuantityMeasurement import *


def test_givenZeroFtAndZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurer(Lengths.Feet, 0.0)
    second_feet = QuantityMeasurer(Lengths.Feet, 0.0)
    assert first_feet == second_feet


def test_givenZeroFtAndNull_WhenCompared_ShouldReturnFalse():
    feet = QuantityMeasurer(Lengths.Feet, 0.0)
    assert feet is not None


def test_givenTwoFeetInstanceVariable_WhenComparedForReference_ShouldReturnTrue():
    first_feet = QuantityMeasurer(Lengths.Feet, 0.0)
    second_feet = first_feet
    assert first_feet is second_feet


def test_givenZeroFeetAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurer(Lengths.Feet, 0.0)
    second_feet = float(0.0)
    assert first_feet != second_feet


def test_givenOneFtAndOneFt_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurer(Lengths.Feet, 1.0)
    second_feet = QuantityMeasurer(Lengths.Feet, 1.0)
    assert first_feet == second_feet


def test_givenOneFtAndTwoFt_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurer(Lengths.Feet, 1.0)
    second_feet = QuantityMeasurer(Lengths.Feet, 2.0)
    assert first_feet is not second_feet


def test_givenZeroInchAndZeroInch_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurer(Lengths.Inch, 0.0)
    second_inch = QuantityMeasurer(Lengths.Inch, 0.0)
    assert first_inch == second_inch


def test_givenZeroInchAndNone_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurer(Lengths.Inch, 0.0)
    assert first_inch != None


def test_givenTwoInchInstanceVraiables_WhenComparedForReference_ShouldReturnTrue():
    first_inch = QuantityMeasurer(Lengths.Inch, 0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_givenZeroInchAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurer(Lengths.Inch, 0.0)
    second_inch = float(0.0)
    assert first_inch != second_inch


def test_givenOneInchAndOneInch_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurer(Lengths.Inch, 1.0)
    second_inch = QuantityMeasurer(Lengths.Inch, 1.0)
    assert first_inch == second_inch


def test_givenOneInchAndTwoInch_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurer(Lengths.Inch, 1.0)
    second_inch = QuantityMeasurer(Lengths.Inch, 2.0)
    assert first_inch != second_inch


def test_givenOneFtAndTwelveInch_WhenCompared_ShouldReturnTrue():
    feet = QuantityMeasurer(Lengths.Feet, 1.0)
    inch = QuantityMeasurer(Lengths.Inch, 12.0)
    assert feet.compare(inch) == True
