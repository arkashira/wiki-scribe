from datetime import datetime, timedelta
from analytics import Analytics, PaidUser

def test_get_new_paid_users():
    analytics = Analytics()
    analytics.add_paid_user(1, datetime.now())
    analytics.add_paid_user(2, datetime.now() - timedelta(days=31))
    new_paid_users = analytics.get_new_paid_users(30)
    assert len(new_paid_users) == 1

def test_get_paid_conversion_metrics():
    analytics = Analytics()
    analytics.add_paid_user(1, datetime.now())
    analytics.add_paid_user(2, datetime.now())
    metrics = analytics.get_paid_conversion_metrics()
    assert metrics == 2

def test_get_paid_conversion_metrics_empty():
    analytics = Analytics()
    metrics = analytics.get_paid_conversion_metrics()
    assert metrics == 0
