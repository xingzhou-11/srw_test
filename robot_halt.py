from rf_protocol import rf_protocol
from robot_rf_command import robot_rf_command
from rf_parameters import parameters
from wait_list import wait_list
import argparse

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("robot_rf_addr", help="Rf address of the robot.", type = str)
parser.add_argument("getway_ip", help="IP address of the gateway.", type = str)
parser.add_argument("command", help="halt or resume.", type = str)
args = parser.parse_args()

def main(robot: robot_rf_command, command: str):
    if command == "halt":
        parameters.halt_action["cmd"] = rf_protocol.ENUM_HALT_ACTION_CMD.HALT_CMD_HALT.value["value"]
        parameters.halt_action["wait"] = wait_list.halt_atcion[0x01]
    else:
        parameters.halt_action["cmd"] = rf_protocol.ENUM_HALT_ACTION_CMD.HALT_CMD_RESUME.value["value"]
        parameters.halt_action["wait"] = wait_list.halt_atcion[0x00]

    robot.robot_halt_action_command()

if __name__ == "__main__":
    robot_command = robot_rf_command(args.robot_rf_addr, args.getway_ip)
    main(robot_command, args.command)