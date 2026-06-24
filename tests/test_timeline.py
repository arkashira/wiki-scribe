import sys
sys.path.insert(0, '../src')
from timeline import TimelineEvent, load_timeline, validate_timeline, store_timeline, display_timeline
import pytest
import json
from tempfile import TemporaryDirectory

def test_load_timeline_valid():
    with TemporaryDirectory() as tmpdir:
        file_path = f"{tmpdir}/timeline.json"
        with open(file_path, 'w') as file:
            json.dump([{'book': 'Book 1', 'chapter': 1}, {'book': 'Book 2', 'chapter': 2}], file)
        timeline = load_timeline(file_path)
        assert len(timeline) == 2
        assert timeline[0].book == 'Book 1'
        assert timeline[0].chapter == 1
        assert timeline[1].book == 'Book 2'
        assert timeline[1].chapter == 2

def test_load_timeline_invalid_json():
    with TemporaryDirectory() as tmpdir:
        file_path = f"{tmpdir}/timeline.json"
        with open(file_path, 'w') as file:
            file.write('Invalid JSON')
        with pytest.raises(ValueError) as e:
            load_timeline(file_path)
        assert str(e.value).startswith("Invalid JSON: ")

def test_load_timeline_invalid_schema():
    with TemporaryDirectory() as tmpdir:
        file_path = f"{tmpdir}/timeline.json"
        with open(file_path, 'w') as file:
            json.dump({'book': 'Book 1', 'chapter': 1}, file)
        with pytest.raises(ValueError) as e:
            load_timeline(file_path)
        assert str(e.value) == "Invalid JSON schema: expected a list"

def test_validate_timeline_empty():
    timeline = []
    with pytest.raises(ValueError) as e:
        validate_timeline(timeline)
    assert str(e.value) == "Timeline is empty"

def test_store_timeline():
    timeline = [TimelineEvent('Book 1', 1), TimelineEvent('Book 2', 2)]
    stored_timeline = store_timeline(timeline)
    assert stored_timeline == {'timeline': [{'book': 'Book 1', 'chapter': 1}, {'book': 'Book 2', 'chapter': 2}]}

def test_display_timeline():
    timeline = [TimelineEvent('Book 1', 1), TimelineEvent('Book 2', 2)]
    displayed_timeline = display_timeline(timeline)
    assert displayed_timeline == "Book 1: 1\nBook 2: 2"

def test_store_timeline_empty():
    timeline = []
    stored_timeline = store_timeline(timeline)
    assert stored_timeline == {'timeline': []}

def test_display_timeline_empty():
    timeline = []
    displayed_timeline = display_timeline(timeline)
    assert displayed_timeline == ""
