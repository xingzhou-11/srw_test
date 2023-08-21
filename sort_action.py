from rf_protocol import rf_protocol
from robot_rf_command import robot_rf_command
from rf_parameters import parameters
from wait_list import wait_list
import argparse
import signal
import time
import sys

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("robot_rf_addr", help="Rf address of the robot.", type = str)
parser.add_argument("getway_ip", help="IP address of the gateway.", type = str)
parser.add_argument("sort_action_command", help="The operation to be performed, load_a, load_b, unload_a, unload_b", type = str)

args = parser.parse_args()

robot_command = robot_rf_command(args.robot_rf_addr, args.getway_ip)

def sort_action():
    robot_action = {
        "read_state": 0x00,
        "load_a": 0x01,
        "load_b": 0x02,
        "unload_a": 0x05,
        "unload_b": 0x06
    }

    parameters.sort_action['cmd'] = robot_action[args.sort_action_command]

    if parameters.sort_action["cmd"] in [0x00]:
        parameters.sort_action["wait"] = wait_list.sort_action[0x00]
    elif parameters.sort_action["cmd"] in [0x01, 0x02]:
        parameters.sort_action["wait"] = wait_list.sort_action[0x01]
    elif parameters.sort_action["cmd"] in [0x05, 0x06]:
        parameters.sort_action["wait"] = wait_list.sort_action[0x05]
    else:
        print(f'command {args.sort_action_command} error')
        sys.exit(0)

    robot_command.sort_action_command()

def circular_load_and_unload():
    """sort机器人装卸货

    Args:
        rf_address (str): 机器人rf地址
        gateway_ip (str): 网关IP地址
        action_command (int): 要进行的命令
        force_unload_flag (int): 附加信息
    """

    robot_action = {
        "read_state": 0x00,
        "load_a": 0x01,
        "load_b": 0x02,
        "unload_a": 0x05,
        "unload_b": 0x06
    }

    for i in range(200):
        
        if parameters.sort_action['cmd'] == 0x01:
            parameters.sort_action['cmd'] = 0x05
        elif parameters.sort_action['cmd'] == 0x02:
            parameters.sort_action['cmd'] = 0x06
        elif parameters.sort_action['cmd'] == 0x02:
            parameters.sort_action['cmd'] = 0x06
        elif parameters.sort_action['cmd'] == 0x05:
            parameters.sort_action['cmd'] = 0x02
        elif parameters.sort_action['cmd'] == 0x06:
            parameters.sort_action['cmd'] = 0x01
        else:
            parameters.sort_action['cmd'] = 0x01

        if parameters.sort_action["cmd"] in [0x00]:
            parameters.sort_action["wait"] = wait_list.sort_action[0x00]
        elif parameters.sort_action["cmd"] in [0x01, 0x02]:
            parameters.sort_action["wait"] = wait_list.sort_action[0x01]
        elif parameters.sort_action["cmd"] in [0x05, 0x06]:
            parameters.sort_action["wait"] = wait_list.sort_action[0x05]
        else:
            print(f'command {args.sort_action_command} error')
            sys.exit(0)
        
        
        sort_state = robot_command.sort_action_command()
        if sort_state in [rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_TIME_MOTOR_ERROR.value['value'], 
                        rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_TIME_MOTOR_ERROR.value['value']]:
            print(f'Error: {parameters.sort_action["cmd"]}')
            sys.exit(0)

        print('i:', i)
        time.sleep(1)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)

    sort_action()
    # circular_load_and_unload()
