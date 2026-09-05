from log_analyzer import analyze_log_file
from log_analyzer import get_health_status


def test_log_analysis():

    info, warning, error = analyze_log_file("app.log")

    assert info == 4
    assert warning == 2
    assert error == 2


def test_health_with_errors():

    assert get_health_status(2) == "ATTENTION"


def test_health_without_errors():

    assert get_health_status(0) == "NORMAL"
