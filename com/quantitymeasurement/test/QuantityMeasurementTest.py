from com.quantitymeasurement.src.QuantityMeasurement import Feet, Inch


def test_givenZeroFtAndZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet


def test_givenZeroFtAndNull_WhenCompared_ShouldReturnFalse():
    feet = Feet(0.0)
    assert feet is not None


def test_givenTwoFeetInstanceVariable_WhenComparedForReference_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet


def test_givenZeroFeetAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(0.0)
    second_feet = float(0.0)
    assert first_feet is not second_feet


def test_givenOneFtAndOneFt_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(1.0)
    second_feet = Feet(1.0)
    assert first_feet is not second_feet


def test_givenOneFtAndTwoFt_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(1.0)
    second_feet = Feet(2.0)
    assert first_feet is not second_feet


def test_givenZeroInchAndZeroInch_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = Inch(0.0)
    assert first_inch == second_inch


def test_givenZeroInchAndNone_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(0.0)
    assert first_inch is not None


def test_givenTwoInchInstanceVraiables_WhenComparedForReference_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_givenZeroInchAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(0.0)
    second_inch = float(0.0)
    assert first_inch is not second_inch


def test_givenOneInchAndOneInch_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(1.0)
    second_inch = Inch(1.0)
    assert first_inch == second_inch


def test_givenOneInchAndTwoInch_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(1.0)
    second_inch = Inch(2.0)
    assert first_inch is not second_inch
