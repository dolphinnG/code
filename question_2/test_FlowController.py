
import pytest
from FlowController import FlowController

# def test_initial_valve_position():
#     controller = FlowController(target_flow=10.0)
#     assert controller.valve_position == 50.0

def test_adjust_knob_with_linear_flowrates():
    controller = FlowController(target_flow=10.0, kp=1.5, ki=0.2, kd=0.1)
    actual_flowrate_readings = [5.0, 7.0, 9.0, 11, 13, 15]
    expected_valve_positions = [59, 64.9, 68.0, 67.9, 64.2, 56.50]  
    print("Linear Flowrates Test")
    for i, flow in enumerate(actual_flowrate_readings):
        valve_position = controller.adjust_knob(flow)
        print(f"Minute {i + 1}: Current Flow = {flow} m³/min, Valve Position = {valve_position:.2f}%")
        assert round(valve_position, 2) == expected_valve_positions[i]

def test_adjust_knob_with_abrupt_flowrates():
    controller = FlowController(target_flow=10.0, kp=1.5, ki=0.2, kd=0.1)
    actual_flowrate_readings = [5.0, 7.0, 9.0, 11, 13, 15, 0, 0, 1.5]
    expected_valve_positions = [59, 64.9, 68.0, 67.9, 64.2, 56.50, 75.0, 94.0, 100]  
    print("Abrupt Flowrates Test")
    for i, flow in enumerate(actual_flowrate_readings):
        valve_position = controller.adjust_knob(flow)
        print(f"Minute {i + 1}: Current Flow = {flow} m³/min, Valve Position = {valve_position:.2f}%")
        assert round(valve_position, 2) == expected_valve_positions[i]

def test_valve_position_limits():
    controller = FlowController(target_flow=10.0, kp=100.0, ki=50.0, kd=25.0)
    actual_flowrate_readings = [0.0, 20.0]  # Extreme values to test limits
    print("Valve Position Limits Test")
    for flow in actual_flowrate_readings:
        valve_position = controller.adjust_knob(flow)
        print(f"Current Flow = {flow:.2f} m³/min, Valve Position = {valve_position:.2f}%")
        assert 0.0 <= valve_position <= 100.0

if __name__ == "__main__":
    pytest.main(['-s'])