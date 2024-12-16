import time


class RateLimiter:
    def __init__(self, limit: int, window_minutes: int = 1):
        """
        Initialize rate limiter
        Args:
            limit: Maximum number of requests allowed per time window
            window_minutes: Time window in minutes
        """
        self.limit = limit
        self.window = window_minutes * 60
        self.user_requests = {}

    def is_allowed(self, user_id: str) -> bool:
        current_time = time.time()
        if user_id not in self.user_requests:
            self.user_requests[user_id] = []

        # Filter out timestamps that are outside the time window
        self.user_requests[user_id] = [
            timestamp
            for timestamp in self.user_requests[user_id]
            if current_time - timestamp < self.window
        ]

        if len(self.user_requests[user_id]) < self.limit:
            self.user_requests[user_id].append(current_time)
            return True
        else:
            return False # drop the request if the limit is exceeded
