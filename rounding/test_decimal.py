import decimal

def test_round_up():
    dec = decimal.Decimal('1.57')
    assert dec.quantize(decimal.Decimal('2.'), rounding=decimal.ROUND_HALF_EVEN).compare(decimal.Decimal('2')) == 0
