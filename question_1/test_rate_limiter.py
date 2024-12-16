
import pytest
import time
from question_1.RateLimiter import RateLimiter

@pytest.fixture
def rate_limiter():
    return RateLimiter(limit=3, window_minutes=1)

def test_is_allowed_below_limit(rate_limiter):
    assert rate_limiter.is_allowed("user1") == True
    assert rate_limiter.is_allowed("user1") == True
    assert rate_limiter.is_allowed("user1") == True

def test_is_allowed_exceed_limit(rate_limiter):
    rate_limiter.is_allowed("user1")
    rate_limiter.is_allowed("user1")
    rate_limiter.is_allowed("user1")
    assert rate_limiter.is_allowed("user1") == False

def test_is_allowed_after_window(rate_limiter):
    rate_limiter.is_allowed("user1")
    rate_limiter.is_allowed("user1")
    rate_limiter.is_allowed("user1")
    time.sleep(61)  # Wait for the window to expire, this will make the test sleep for 61 seconds, make sure to wait
    assert rate_limiter.is_allowed("user1") == True