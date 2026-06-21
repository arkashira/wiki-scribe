import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class PaidUser:
    user_id: int
    conversion_date: datetime

class Analytics:
    def __init__(self):
        self.analytics_table = []

    def add_paid_user(self, user_id, conversion_date):
        self.analytics_table.append(PaidUser(user_id, conversion_date))

    def get_new_paid_users(self, days):
        cutoff_date = datetime.now() - timedelta(days=days)
        return [user for user in self.analytics_table if user.conversion_date >= cutoff_date]

    def get_paid_conversion_metrics(self):
        new_paid_users = self.get_new_paid_users(30)
        return len(new_paid_users)
