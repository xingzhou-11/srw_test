#!/usr/bin/env python3
from rf_protocol import rf_protocol
from robot_rf_command import *
import argparse

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("robot_rf_addr", help="Rf address of the robot.", type = str)
parser.add_argument("getway_ip", help="IP address of the gateway.", type = str)
parser.add_argument("absolute_target", help="The position to be achieved.", type = str)
parser.add_argument("velocity_in_counts", help="target velocity.", type = str)
args = parser.parse_args()

def robot_moving():
    """机器人移动

    Args:
        rf_address (str): 机器人rf地址
        gateway_ip (str): 网关IP地址
        absolute_target (int): 要到达的位置
        velocity_in_counts (int): 目标速度
    """

    robot = robot_rf_command(args.robot_rf_addr, args.getway_ip)

    parameters.moving["absolute_target"] = int(args.absolute_target * 16000)
    parameters.moving["velocity_in_counts"] = int(args.velocity_in_counts * 16000)
    parameters.moving["acceleration_in_counts"] = int(3.5 * 85000)
    parameters.moving["deceleration_in_counts"] = int(3.5 * 85000)

    parameters.moving["self-correct"] = 0
    parameters.moving["reset_position_check"] = 0
    parameters.moving["enter_lier"] = 0

    robot.srw_moving_command()


if __name__ == "__main__":
    
    robot_moving()
