from mbti_explorer import classify, explain


def test_classify_maps_each_dimension():
    assert classify(["A", "B", "A", "B"]) == "ENTP"


def test_explain_is_readable():
    text = explain("ISTJ")
    assert "detail-oriented" in text
    assert "planful" in text


def test_invalid_answers_fail_loudly():
    try:
        classify(["A", "B"])
    except ValueError as error:
        assert "exactly four" in str(error)
    else:
        raise AssertionError("invalid answers should raise ValueError")
