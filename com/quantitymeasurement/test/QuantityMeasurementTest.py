from com.quantitymeasurement.src.QuantityMeasurement import *


def test_givenZeroFtAndZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurer(Lengths.FEET, 0.0)
    second_feet = QuantityMeasurer(Lengths.FEET, 0.0)
    assert first_feet == second_feet


def test_givenZeroFtAndNull_WhenCompared_ShouldReturnFalse():
    feet = QuantityMeasurer(Lengths.FEET, 0.0)
    assert feet is not None


def test_givenTwoFeetInstanceVariable_WhenComparedForReference_ShouldReturnTrue():
    first_feet = QuantityMeasurer(Lengths.FEET, 0.0)
    second_feet = first_feet
    assert first_feet is second_feet


def test_givenZeroFeetAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurer(Lengths.FEET, 0.0)
    second_feet = float(0.0)
    assert first_feet != second_feet


def test_givenOneFtAndOneFt_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurer(Lengths.FEET, 1.0)
    second_feet = QuantityMeasurer(Lengths.FEET, 1.0)
    assert first_feet == second_feet


def test_givenOneFtAndTwoFt_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurer(Lengths.FEET, 1.0)
    second_feet = QuantityMeasurer(Lengths.FEET, 2.0)
    assert first_feet is not second_feet


def test_givenZeroInchAndZeroInch_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurer(Lengths.INCH, 0.0)
    second_inch = QuantityMeasurer(Lengths.INCH, 0.0)
    assert first_inch == second_inch


def test_givenZeroInchAndNone_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurer(Lengths.INCH, 0.0)
    assert first_inch != None


def test_givenTwoInchInstanceVraiables_WhenComparedForReference_ShouldReturnTrue():
    first_inch = QuantityMeasurer(Lengths.INCH, 0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_givenZeroInchAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurer(Lengths.INCH, 0.0)
    second_inch = float(0.0)
    assert first_inch != second_inch


def test_givenOneInchAndOneInch_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurer(Lengths.INCH, 1.0)
    second_inch = QuantityMeasurer(Lengths.INCH, 1.0)
    assert first_inch == second_inch


def test_givenOneInchAndTwoInch_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurer(Lengths.INCH, 1.0)
    second_inch = QuantityMeasurer(Lengths.INCH, 2.0)
    assert first_inch != second_inch


def test_givenOneFtAndTwelveInch_WhenCompared_ShouldReturnTrue():
    feet = QuantityMeasurer(Lengths.FEET, 1.0)
    inch = QuantityMeasurer(Lengths.INCH, 12.0)
    assert feet.compare(inch)


def test_givenTwelveInchAndOneFeet_WhenCompared_ShouldReturnTrue():
    feet = QuantityMeasurer(Lengths.FEET, 1.0)
    inch = QuantityMeasurer(Lengths.INCH, 12.0)
    assert inch.compare(feet)


def test_giveOneYardAndOneYard_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurer(Lengths.YARD, 1.0)
    second_yard = QuantityMeasurer(Lengths.YARD, 1.0)
    assert first_yard.compare(second_yard)


def test_givenThreeFtAndOneYard_WhenCompared_ShouldReturnTrue():
    feet = QuantityMeasurer(Lengths.FEET, 3.0)
    yard = QuantityMeasurer(Lengths.YARD, 1.0)
    assert feet.compare(yard)


def test_givenOneFtAndOneYard_WhenCompared_ShouldReturnFalse():
    feet = QuantityMeasurer(Lengths.FEET, 1.0)
    yard = QuantityMeasurer(Lengths.YARD, 1.0)
    assert feet.compare(yard) == False


def test_givenOneInchAndOneYard_WhenCompared_ShouldReturnFalse():
    inch = QuantityMeasurer(Lengths.INCH, 1.0)
    yard = QuantityMeasurer(Lengths.YARD, 1.0)
    assert not inch.compare(yard)


def test_givenOneYardAndThirtySixInch_WhenCompared_ShouldReturnTrue():
    inch = QuantityMeasurer(Lengths.INCH, 36.0)
    yard = QuantityMeasurer(Lengths.YARD, 1.0)
    assert inch.compare(yard)


def test_givenOneCmAndOneCm_WhenCompared_ShouldReturnTrue():
    first_cm = QuantityMeasurer(Lengths.CM, 1.0)
    second_cm = QuantityMeasurer(Lengths.CM, 1.0)
    assert first_cm.compare(second_cm)


def test_givenTwoInchAndFiveCm_WhenCompared_ShouldReturnTrue():
    inch = QuantityMeasurer(Lengths.INCH, 2.0)
    cm = QuantityMeasurer(Lengths.CM, 5.0)
    assert inch.compare(cm)


def test_givenOneInchAndOneCm_WhenCompared_ShouldReturnFalse():
    inch = QuantityMeasurer(Lengths.INCH, 1.0)
    cm = QuantityMeasurer(Lengths.CM, 1.0)
    assert not inch.compare(cm)


def test_givenOneFeetAndThirtyCm_WhenCompared_ShouldReturnTrue():
    feet = QuantityMeasurer(Lengths.FEET, 1.0)
    cm = QuantityMeasurer(Lengths.CM, 30.0)
    assert feet.compare(cm)


def test_givenOneYardAndNinetyCm_WhenCompared_ShouldReturnTrue():
    yard = QuantityMeasurer(Lengths.YARD, 1.0)
    cm = QuantityMeasurer(Lengths.CM, 90.0)
    assert yard.compare(cm)


def test_givenOneInchAndOneInch_WhenAdded_ShouldReturnSumInInches():
    first_inch = QuantityMeasurer(Lengths.INCH, 1.0)
    second_inch = QuantityMeasurer(Lengths.INCH, 1.0)
    assert first_inch.add(second_inch) == 2.0


def test_givenOneftAndTwoInch_WhenAdded_ShouldReturnSumInInches():
    inch = QuantityMeasurer(Lengths.INCH, 2.0)
    feet = QuantityMeasurer(Lengths.FEET, 1.0)
    assert inch.add(feet) == 14.0


def test_givenOneFtAndOneFt_WhenAdded_ShouldReturnSumInInches():
    first_feet = QuantityMeasurer(Lengths.FEET, 1.0)
    second_feet = QuantityMeasurer(Lengths.FEET, 1.0)
    assert first_feet.add(second_feet) == 24.0


def test_givenTwoInchAndTwoPointFiveCm_WhenAdded_ShouldReturnSumInInches():
    inch = QuantityMeasurer(Lengths.INCH, 2.0)
    cm = QuantityMeasurer(Lengths.CM, 2.5)
    assert inch.add(cm) == 3.0


def test_givenOneLitreAndOneLitre_WhenCompared_ShouldReturnTrue():
    first_litre = QuantityMeasurer(Volumes.LITRE, 1.0)
    second_litre = QuantityMeasurer(Volumes.LITRE, 1.0)
    assert first_litre == second_litre


def test_givenOneGallonAndThreePointSeven_WhenCompared_ShouldReturnTrue():
    gallon = QuantityMeasurer(Volumes.GALLON, 1.0)
    litre = QuantityMeasurer(Volumes.LITRE, 3.78)
    assert gallon.compare(litre)


def test_givenOneLitreAndThousandMl_WhenCompared_ShouldReturnTrue():
    litre = QuantityMeasurer(Volumes.LITRE, 1.0)
    ml = QuantityMeasurer(Volumes.ML, 1000.0)
    assert litre.compare(ml)


def test_givenOneGallaonAndThreePointSevenLitre_WhenAdded_ShouldReturnSumInLitres():
    litre = QuantityMeasurer(Volumes.LITRE, 3.78)
    gallon = QuantityMeasurer(Volumes.GALLON, 1.0)
    assert litre.add(gallon) == 7.56


def test_givenOneLitreAndThousandMl_WhenAdded_ShouldReturnSumInLitres():
    litre = QuantityMeasurer(Volumes.LITRE, 1.0)
    ml = QuantityMeasurer(Volumes.ML, 1000.0)
    assert litre.add(ml) == 2.0


def test_givenOneKgAndOneKg_WhenCompared_ShouldRreturnTrue():
    first_kg = QuantityMeasurer(Weights.KG, 1.0)
    second_kg = QuantityMeasurer(Weights.KG, 1.0)
    assert first_kg.compare(second_kg)


def test_givenOneKgAndThousandGrams_WhenCompared_ShouldRreturnTrue():
    kg = QuantityMeasurer(Weights.KG, 1.0)
    grams = QuantityMeasurer(Weights.GRAMS, 1000.0)
    assert kg.compare(grams)


def test_givenOneTonneAndThousandKg_WhenCompared_ShouldRreturnTrue():
    tonne = QuantityMeasurer(Weights.TONNE, 1.0)
    kg = QuantityMeasurer(Weights.KG, 1000.0)
    assert kg.compare(tonne)


def test_given_oneTonneAndThousandGram_WhenAdded_ShouldReturnSumInKgs():
    tonne = QuantityMeasurer(Weights.TONNE, 1.0)
    kg = QuantityMeasurer(Weights.GRAMS, 1000.0)
    assert kg.add(tonne) == 1001.0
