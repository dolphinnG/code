# Question #2: Design a Flow Control System

## Background
There is a water distribution system where water flows from a reservoir to a village through a control valve. The system includes a flow meter that measures the volumetric flow rate every minute.

## Task
Design a control algorithm that maintains a stable volumetric flow rate by automatically adjusting the control valve position.

## Specifications
- **Input**: Current flow rate measurement (m³/minute), target flow rate
- **Sampling and Controlling frequency**: Every minute
- **Output**: Control valve position (0-100%)
    - 0% = Fully closed
    - 100% = Fully open

## Requirements
- Write a control algorithm that takes the current flow measurement as input and outputs the appropriate valve position.
- The system should maintain a steady target flow rate as much as possible.
- Handle edge cases and potential system disturbances.

## Assumptions
- There is no delay from the valve change to the flow rate change.

```python
class FlowController:
        def __init__(self, target_flow: float):
                """
                Initialize controller
                Args:
                        target_flow: Desired flow rate in volume/minute
                """

        def adjust_knob(self, current_flow: float) -> float:
                """
                Calculate new knob position
                Args:
                        current_flow: Measured flow rate in volume/minute
                Returns:
                        float: New knob position (0-100)
                """
```
