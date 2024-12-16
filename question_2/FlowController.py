import random

class FlowController:
    def __init__(self, target_flow: float, kp: float = 1.0, ki: float = 0.1, kd: float = 0.05):
        """
        Initialize controller.
        Args:
            target_flow: Desired flow rate in volume/minute.
            kp: Proportional gain.
            ki: Integral gain.
            kd: Derivative gain.
        """
        self.target_flow = target_flow
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.prev_error = 0.0  
        self.integral = 0.0   # accumulation of errors
        self.valve_position = 50.0  # init neutral position

    def adjust_knob(self, current_flow: float) -> float:
        """
        Calculate new knob position.
        Args:
            current_flow: Measured flow rate in volume/minute.
        Returns:
            float: New knob position (0-100).
        """
        error = self.target_flow - current_flow
        self.integral += error
        derivative = error - self.prev_error

        # Proportional–integral–derivative output
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

        # Adjust valve position 
        self.valve_position += output

        # Clampp the valve position to be between 0-100%
        self.valve_position = max(0.0, min(100.0, self.valve_position))

        # Update the previous error for the next calculation
        self.prev_error = error

        return self.valve_position


