from rf_protocol import *
from robot_rf_command import *
import argparse
import logging
import time

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("robot_rf_addr", help="Rf address of the robot.", type = str)
parser.add_argument("getway_ip", help="IP address of the gateway.", type = str)
# parser.add_argument("absolute_target", help="This is the target location.", type = float)
# parser.add_argument('velocity_in_counts', help="This is the target velocity.", type = float)
# parser.add_argument('acceleration_in_counts', help="This is the target acceleration.", type = float)
# parser.add_argument('deceleration_in_counts', help="This is the target deceleration.", type = float)
args = parser.parse_args()

robot = robot_rf_command(args.robot_rf_addr, args.getway_ip)

def DLOG(log_file_name:str, log_msg: str):
    """DLOG

    Args:
        log_file_name (str): log file name
        level (int): level
        log_msg (str): log msg
    """
    logging.basicConfig(filename=log_file_name, level=logging.INFO)
    logging.info(log_msg)

def SRW_move(absolute_target, velocity_in_counts, acceleration_in_counts, deceleration_in_counts, self_correct=0):
    """SRW_移动

    Args:
        robot_rf_addr (str): 机器人rf地址
        getway_ip (str): 网关rf地址
        function_code (int): 功能码
        absolute_target (int): 绝对位置
        velocity_in_counts (int): 最大速度
        acceleration_in_counts (int): 加速度
        deceleration_in_counts (int): 减速度
        self_correct (int): 自我修正, 打开输入1
        Reset_position_check (int): 复位位置差, 打开输入1
        enter_lifter (int): 进入升降机, 打开输入1
    """
    
    parameters.moving["absolute_target"] = int(absolute_target * 16000)
    parameters.moving["velocity_in_counts"] = int(velocity_in_counts * 16000)
    parameters.moving["acceleration_in_counts"] = int(acceleration_in_counts * 85000)
    parameters.moving["deceleration_in_counts"] = int(deceleration_in_counts * 85000)
    parameters.moving["self-correct"] = self_correct
    
    pos = robot.srw_moving_command()
    while abs(pos - parameters.moving["absolute_target"]) > 200:
        pos = robot.srw_moving_command()

def run():
    # SRW_move(1.2, 0.1, 3.6, 3.6, self_correct=1)
    time.sleep(1)

    for i in range(60):
        print(i)
        SRW_move(0, 4, 3.5, 3.5, self_correct=0)
        # SRW_move(8.7,  4,   3.6, 3.6, self_correct=1)
        # SRW_move(9.2,  0.1, 3.6, 3.6, self_correct=1)
        time.sleep(1)

        SRW_move(-3, 4, 3.5, 3.5, self_correct=0)
        # SRW_move(1.7, 4,   3.6, 3.6, self_correct=1)
        # SRW_move(1.2, 0.1, 3.6, 3.6, self_correct=1)
        time.sleep(1)

if __name__ == "__main__":
    run()
