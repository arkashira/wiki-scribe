from wiki_scribe import WikiScribe, AutoApprovedPage
import pytest
from datetime import datetime, timedelta

@pytest.fixture
def wiki_scribe():
    data = [
        AutoApprovedPage("Project1", "2022-01-01", 10),
        AutoApprovedPage("Project1", "2022-01-02", 20),
        AutoApprovedPage("Project2", "2022-01-01", 30),
        AutoApprovedPage("Project2", "2022-01-02", 40),
    ]
    return WikiScribe(data)

def test_get_monthly_trend(wiki_scribe):
    trend = wiki_scribe.get_monthly_trend()
    assert trend == {"2022-01": 100}

def test_get_monthly_trend_with_project(wiki_scribe):
    trend = wiki_scribe.get_monthly_trend(project="Project1")
    assert trend == {"2022-01": 30}

def test_get_monthly_trend_with_date_range(wiki_scribe):
    trend = wiki_scribe.get_monthly_trend(start_date="2022-01-01", end_date="2022-01-01")
    assert trend == {"2022-01": 40}

def test_refresh_data(wiki_scribe):
    new_data = [
        AutoApprovedPage("Project1", "2022-01-03", 50),
        AutoApprovedPage("Project2", "2022-01-03", 60),
    ]
    wiki_scribe.refresh_data(new_data)
    trend = wiki_scribe.get_monthly_trend()
    assert trend == {"2022-01": 110}

def test_filter_by_project_and_date_range(wiki_scribe):
    filtered_data = wiki_scribe.filter_by_project_and_date_range("Project1", "2022-01-01", "2022-01-02")
    assert len(filtered_data) == 2
    assert filtered_data[0].project == "Project1"
    assert filtered_data[0].date == "2022-01-01"
    assert filtered_data[0].count == 10
    assert filtered_data[1].project == "Project1"
    assert filtered_data[1].date == "2022-01-02"
    assert filtered_data[1].count == 20
