from rf_protocol import rf_protocol
from robot_rf_command import robot_rf_command
from rf_parameters import parameters
import argparse
import sys

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("robot_rf_addr", help="Rf address of the robot.", type = str)
parser.add_argument("getway_ip", help="IP address of the getway.", type = str)
args = parser.parse_args()

def ping_online():
    """机器人ping命令
    """
    pass

if __name__ == "__main__":
    robot_command = robot_rf_command(args.robot_rf_addr, args.getway_ip)
    robot_command.ping_command()