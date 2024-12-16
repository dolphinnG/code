
# Question #1: Design a Rate Limiting System

## Background
In high-traffic web services, it's crucial to protect backend resources from being overwhelmed by implementing rate limiting mechanisms. Each user of the system needs to be monitored and controlled independently.

## Task
Design a rate limiter that restricts the number of requests a user can make within a specified time window.

## Specifications
- **Input**: User identifier (string)
- **Output**: Boolean (true if request is allowed, false if rate limit exceeded)
- **Time window**: 1 minute (configurable)
- **Request limit**: N requests per time window (configurable)

## Requirements
- Implement a system that tracks requests per user over the specified time window.
- Return true if the user has not exceeded their limit, false otherwise.
- Clean up old data to prevent memory leaks.

