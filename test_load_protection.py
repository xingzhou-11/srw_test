#!/usr/bin/env python3
from rf_protocol import rf_protocol
from rf_parameters import parameters
from robot_rf_command import robot_rf_command
import pytest
import allure
import os
import time

robot = robot_rf_command('1BB1FC', '10.0.66.122')
robot.ping_command()

@allure.feature('moving in load')
@pytest.mark.parametrize('cmd1, cmd2, wait1, wait2, abs_target, action', [
    (0x01, 0x00, [0x03], [0x03, 0x07], 0.5, 1),
    (0x01, 0x05, [0x03], [0x03, 0x07], 0.5, 0),
    (0x01, 0x06, [0x03], [0x03, 0x07], 0.5, 0),
    (0x01, 0x00, [0x03], [0x03, 0x07], 0.5, 2),
    (0x02, 0x00, [0x03], [0x03, 0x07], 0.5, 1),
    (0x02, 0x05, [0x03], [0x03, 0x07], 0.5, 0),
    (0x02, 0x06, [0x03], [0x03, 0x07], 0.5, 0),
    (0x02, 0x00, [0x03], [0x03, 0x07], 0.5, 2),
    (0x05, 0x00, [0x07], [0x07, 0x03], 0.5, 1),
    (0x05, 0x01, [0x07], [0x07, 0x03], 0.5, 0),
    (0x05, 0x02, [0x07], [0x07, 0x03], 0.5, 0),
    (0x05, 0x00, [0x07], [0x07, 0x03], 0.5, 2),
    (0x06, 0x00, [0x07], [0x07, 0x03], 0.5, 1),
    (0x06, 0x01, [0x07], [0x07, 0x03], 0.5, 0),
    (0x06, 0x02, [0x07], [0x07, 0x03], 0.5, 0),
    (0x06, 0x00, [0x07], [0x07, 0x03], 0.5, 2)
], 
ids=[
    'moving_in_load_a',
    'unload_a_in_load_a',
    'unload_b_in_load_a',
    'halt_in_load_a',
    'moving_in_load_b',
    'unload_a_in_load_b',
    'unload_b_in_load_b',
    'halt_in_load_b',
    'moving_in_unload_a',
    'load_a_in_unload_a',
    'load_b_in_unload_a',
    'halt_in_unload_a',
    'moving_in_unload_b',
    'load_a_in_unload_b',
    'load_b_in_unload_b',
    'halt_in_unload_b'
    ])
def test_moving_in_load(cmd1, cmd2, wait1, wait2, abs_target, action):
    ret = None
    parameters.sort_action['cmd'] = cmd1
    parameters.sort_action['wait'] = wait1
    while robot.sort_action_command() not in [0x03, 0x07]:
        time.sleep(0.1)

    if action == 1:
        print('moving')
        parameters.moving["absolute_target"] = int(abs_target * 16000)
        parameters.moving["velocity_in_counts"] = int(1 * 16000)
        parameters.moving["acceleration_in_counts"] = int(1 * 85000)
        parameters.moving["deceleration_in_counts"] = int(1 * 85000)

        parameters.moving["self-correct"] = 0
        parameters.moving["reset_position_check"] = 0
        parameters.moving["enter_lier"] = 0

        robot.srw_moving_command()
    elif action == 2:
        print('halt')
        parameters.halt_action['cmd'] = 0x01
        parameters.halt_action['wait'] = [0x02]
        ret = robot.robot_halt_action_command()
        assert ret == 0x02

        parameters.halt_action['cmd'] = 0x00
        parameters.halt_action['wait'] = [0x02]
        ret = robot.robot_halt_action_command()
    else:
        print('action')
        parameters.sort_action['cmd'] = cmd2
        parameters.sort_action['wait'] = wait2
        while ret not in wait2:
            ret = robot.sort_action_command()
            time.sleep(0.1)
        assert ret == wait2[0]

    time.sleep(5)

@allure.feature('load in moving')
@pytest.mark.parametrize('abs_target, cmd1, wait1, action', [
    (1, 0x01, [0x01], 0),
    (0, 0x02, [0x01], 0),
    (1, 0x05, [0x01], 0),
    (0, 0x06, [0x01], 0),
    (1, 0x00, [0x00], 1),
    (0, 0x02, [0x01], 0),
],
ids=[
    'load_a_in_move',
    'load_b_in_move',
    'unload_a_in_move',
    'unload_b_in_move',
    'halt_in_move',
    'move_to_0'
])
def test_load_in_moving(abs_target, cmd1, wait1, action):
    ret = None
    parameters.moving["absolute_target"] = int(abs_target * 16000)
    parameters.moving["velocity_in_counts"] = int(1 * 16000)
    parameters.moving["acceleration_in_counts"] = int(1 * 85000)
    parameters.moving["deceleration_in_counts"] = int(1 * 85000)

    parameters.moving["self-correct"] = 0
    parameters.moving["reset_position_check"] = 0
    parameters.moving["enter_lier"] = 0

    robot.srw_moving_command()
    time.sleep(0.5)

    if action == 1:
        parameters.halt_action['cmd'] = 0x01
        parameters.halt_action['wait'] = [0x01]
        ret = robot.robot_halt_action_command()
        assert ret == 0x01

        parameters.halt_action['cmd'] = 0x00
        parameters.halt_action['wait'] = [0x02]
        ret = robot.robot_halt_action_command()
    else:
        parameters.sort_action['cmd'] = cmd1
        parameters.sort_action['wait'] = wait1
        while ret not in wait1:
            ret = robot.sort_action_command()
            time.sleep(0.1)
        assert ret == wait1[0]

    time.sleep(7)

@allure.feature('action in halt')
def test_action_in_halt():
    with allure.step("robot halt"):
        parameters.halt_action['cmd'] = 0x01
        parameters.halt_action['wait'] = [0x01]
        ret = robot.robot_halt_action_command()
        assert ret == 0x01

    with allure.step("load_a in halt"):
        parameters.sort_action['cmd'] = 0x01
        while ret not in [0x01]:
            ret = robot.sort_action_command()
            time.sleep(0.1)
        assert ret == 0x01

    with allure.step("load_b in halt"):
        parameters.sort_action['cmd'] = 0x02
        while ret not in [0x01]:
            ret = robot.sort_action_command()
            time.sleep(0.1)
        assert ret == 0x01

    with allure.step("unload_a in halt"):
        parameters.sort_action['cmd'] = 0x05
        while ret not in [0x01]:
            ret = robot.sort_action_command()
            time.sleep(0.1)
        assert ret == 0x01

    with allure.step("unload_b in halt"):
        parameters.sort_action['cmd'] = 0x06
        while ret not in [0x01]:
            ret = robot.sort_action_command()
            time.sleep(0.1)
        assert ret == 0x01

    parameters.moving["absolute_target"] = 1 * 16000
    parameters.moving["velocity_in_counts"] = 1 * 16000
    parameters.moving["acceleration_in_counts"] = 1 * 85000
    parameters.moving["deceleration_in_counts"] = 1 * 85000

    parameters.moving["self-correct"] = 0
    parameters.moving["reset_position_check"] = 0
    parameters.moving["enter_lier"] = 0

    with allure.step("move in halt"):
        robot.srw_moving_command()

    with allure.step("robot continue"):
        parameters.halt_action['cmd'] = 0x00
        parameters.halt_action['wait'] = [0x02]
        ret = robot.robot_halt_action_command()
        assert ret == 0x02

if __name__ == '__main__':
    pytest.main(['-s', '-q','test_load_protection.py','--clean-alluredir','--alluredir=allure-results'])
    os.system(r"allure generate -c -o allure-report")
