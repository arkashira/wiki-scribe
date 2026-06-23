import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class AutoApprovedPage:
    project: str
    date: str
    count: int

class WikiScribe:
    def __init__(self, data: List[AutoApprovedPage]):
        self.data = data

    def get_monthly_trend(self, project: str = None, start_date: str = None, end_date: str = None):
        filtered_data = [page for page in self.data if (project is None or page.project == project) and 
                         (start_date is None or page.date >= start_date) and 
                         (end_date is None or page.date <= end_date)]
        trend = {}
        for page in filtered_data:
            month = page.date[:7]
            if month not in trend:
                trend[month] = 0
            trend[month] += page.count
        return trend

    def refresh_data(self, new_data: List[AutoApprovedPage]):
        self.data = new_data

    def filter_by_project_and_date_range(self, project: str, start_date: str, end_date: str):
        return [page for page in self.data if page.project == project and start_date <= page.date <= end_date]
