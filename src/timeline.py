import json
from dataclasses import dataclass
from typing import List

@dataclass
class TimelineEvent:
    book: str
    chapter: int

def load_timeline(file_path: str) -> List[TimelineEvent]:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Invalid JSON schema: expected a list")
        timeline = []
        for event in data:
            if not isinstance(event, dict) or 'book' not in event or 'chapter' not in event:
                raise ValueError("Invalid JSON schema: expected a dictionary with 'book' and 'chapter' keys")
            timeline.append(TimelineEvent(event['book'], event['chapter']))
        return timeline
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON: " + str(e))

def validate_timeline(timeline: List[TimelineEvent]) -> None:
    if not timeline:
        raise ValueError("Timeline is empty")
    for event in timeline:
        if not isinstance(event.book, str) or not isinstance(event.chapter, int):
            raise ValueError("Invalid timeline event: book must be a string and chapter must be an integer")

def store_timeline(timeline: List[TimelineEvent]) -> dict:
    return {'timeline': [{'book': event.book, 'chapter': event.chapter} for event in timeline]}

def display_timeline(timeline: List[TimelineEvent]) -> str:
    return '\n'.join(f"{event.book}: {event.chapter}" for event in timeline)
