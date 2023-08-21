from rf_protocol import rf_protocol
from rf_parameters import parameters
from robot_rf_packet import robot_rf_packet
from enum import Enum
import datetime
import logging
import socket
import time
import sys

logging.basicConfig(filename="udp_getway.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class robot_rf_command(robot_rf_packet):
    
    def __init__(self, robot_addr: str, rf_getway_ip: str):
        """robot_rf_command
        Args:
            robot_addr (str): 机器人的rf地址
            rf_getway_ip (str): 网关的ip地址(字符串)
        """
        self.packet = robot_rf_packet(rf_addr=robot_addr)
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.settimeout(0.2)  # 设置udp接收超时时间
        self.udp_address = (rf_getway_ip, 8080)

    def udp_data_parse(self, function_code: int, data_packet: bytes) -> str:
        """UDP数据发送接收解析
        Args:
            function_code (int): 功能码
            data_packet (bytes): 数据包
        Returns:
            _type_: str
        """
        try:
            parameters.Batch_Number += 1
            if parameters.Batch_Number > parameters.Batch_Number_Max:
                parameters.Batch_Number = 1
            self.udp_socket.sendto(data_packet, self.udp_address)
            logger.info("send:" + data_packet.hex(":"))
            recv_msg, _ = self.udp_socket.recvfrom(1024)
            logger.info("recv:" + recv_msg.hex(":"))

            if int(recv_msg[5]) == function_code:
                for func in rf_protocol.ENUM_FUNCTION_CODE:
                    if func.value['value'] == recv_msg[5]:
                        return func.value['func'](recv_msg)
        except Exception as e:
            if str(e) != 'timed out':
                return -1

    def robot_state_parse(self, rf_protocol_ENUM: Enum, data: int) -> int:
        """udp数据解析
        Args:
            rf_protocol_ENUM (Enum): 相关枚举
            data (int): 数据处理后返回的数据
        Returns:
            int: robot_state
        """
        for state in rf_protocol_ENUM:
            if state.value["value"] == data:
                print(state)
                return state.value["value"]


    def ping_command(self):
        """机器人ping命令
        """
        function_code = parameters.state["func"]
        state_command = parameters.state["cmd"]
        finally_state_enum = parameters.state["finally_state_enum"]

        send_data = self.packet.robot_ping_package(function_code, state_command)
        recv_data = self.udp_data_parse(function_code, send_data)
        parameters.robot_end_state["enum"] = self.robot_state_parse(finally_state_enum, recv_data)

    def homing_command(self):
        """机器人回原点
        """
        function_code = parameters.homing["func"]
        command = parameters.homing["cmd"]
        finally_state_enum = parameters.homing["finally_state_enum"]
        wait = parameters.homing["wait"]

        send_data = self.packet.robot_homing_package(function_code, command)
        recv_data = None
        while recv_data not in wait and parameters.stop_signal:
            recv_data = self.udp_data_parse(function_code, send_data)
            parameters.robot_end_state["enum"] = self.robot_state_parse(finally_state_enum, recv_data)
            if recv_data == -1:
                sys.exit(0)
        
    def cm0_moving_command(self):
        """CM0移动
        """
        function_code = parameters.moving["func"]
        absolute_target = parameters.moving["absolute_target"]
        velocity_in_counts = parameters.moving["velocity_in_counts"]
        desired_position = parameters.moving["desired_position"]
        
        send_data = self.packet.cm0_moving_package(function_code, absolute_target, velocity_in_counts)
        recv_data = [0] * 4
        while (not abs(desired_position - recv_data[0]) > 100):
            recv_data = self.udp_data_parse(function_code, send_data)
            print(f"position:{recv_data[0]}, velocity:{recv_data[1]}, torque:{recv_data[2]}, info:{recv_data[3]}")
            if recv_data == -1:
                sys.exit(0)

    def srg_moving_command(self):
        """SRG移动
        """
        function_code = parameters.moving["func"]
        absolute_target = parameters.moving["absolute_target"]
        velocity_in_counts = parameters.moving["velocity_in_counts"]

        select_avoidance_direction = parameters.moving["select_avoidance_direction"]<<2
        target_position = parameters.moving["target_position"]<<1
        track_direction = parameters.moving["track_direction"]
        additional_info = select_avoidance_direction + target_position + track_direction

        desired_position = parameters.moving["desired_position"]

        send_data = self.packet.srg_moving_package(function_code, absolute_target, velocity_in_counts, additional_info)
        recv_data = [100] * 3
        while (not abs(desired_position - recv_data[0]) < 100 or recv_data[1] != 0) and parameters.stop_signal:
            recv_data = self.udp_data_parse(function_code, send_data)
            print(f"position:{recv_data[0]}, velocity:{recv_data[1]}, torque:{recv_data[2]}, info:{recv_data[3]}")
            if recv_data == -1:
                sys.exit(0)
    
    def srw_moving_command(self):
        """SRW移动
        """
        function_code = parameters.moving["func"]
        absolute_target = parameters.moving["absolute_target"]
        velocity_in_counts = parameters.moving["velocity_in_counts"]
        acceleration_in_counts = parameters.moving["acceleration_in_counts"]
        deceleration_in_counts = parameters.moving["deceleration_in_counts"]

        self_correct = parameters.moving["self-correct"]<<3
        reset_position_check = parameters.moving["reset_position_check"]<<2
        enter_lier = parameters.moving["enter_lier"]
        additional_info = self_correct + reset_position_check + enter_lier

        desired_position = parameters.moving["desired_position"]

        send_data = self.packet.srw_moving_package(function_code, absolute_target, velocity_in_counts, additional_info, acceleration_in_counts, deceleration_in_counts)
        recv_data = None
        while None == recv_data:
            recv_data = self.udp_data_parse(function_code, send_data)
            if recv_data != None:
                print(f"position:{recv_data[0]}, velocity:{recv_data[1]}, torque:{recv_data[2]}, info:{recv_data[3]}")
                return recv_data[0]
            if recv_data == -1:
                sys.exit(0)

    def sort_action_command(self):
        """sort装卸货
        """
        function_code = parameters.sort_action["func"]
        sort_action_command = parameters.sort_action["cmd"]
        force_unload_flag = parameters.sort_action["force_unload"]
        finally_state_enum = parameters.sort_action["finally_state_enum"]
        wait = parameters.sort_action["wait"]

        send_data = self.packet.sort_action_package(function_code, sort_action_command, force_unload_flag)
        recv_data = None
        while recv_data not in wait:
            recv_data = self.udp_data_parse(function_code, send_data)
            parameters.robot_end_state["enum"] = self.robot_state_parse(finally_state_enum, recv_data)
            if recv_data == -1:
                sys.exit(0)
        return recv_data
        
    def moving_cancel_command(self):
        """主轴停止移动
        """
        function_code = parameters.moving_cancel["func"]

        send_data = self.packet.robot_moving_cancel_package(function_code)
        recv_data = self.udp_data_parse(function_code, send_data)
        print(f"position:{recv_data}")

    def sort_sensor_state_command(self):
        """sort传感器触发状态
        """
        function_code = parameters.sort_sensor_state["func"]

        send_data = self.packet.sort_sensor_state_package(self, function_code)
        recv_data = self.udp_data_parse(function_code, send_data)

        if recv_data != rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]:
            print(f"a_side:{recv_data[0]}, center:{recv_data[1]}, b_side:{recv_data[2]}, homing:{recv_data[3]}, avoidance:{recv_data[4]}, lifter_homing:{recv_data[5]}")
        
    def pick_box_action_command(self):
        """pick拉还箱命令
        """
        function_code = parameters.pick_box_action["func"]
        command = parameters.pick_box_action["cmd"]
        decoupled_absolute_position = parameters.pick_box_action["decoupled_absolute_position"]
        aligned_absolute_position = parameters.pick_box_action["aligned_absolute_position"]
        leave_box_slot_absolute_position = parameters.pick_box_action["leave_box_slot_absolute_position"]

        additional_info_bit_0 = parameters.pick_box_action["column's_direction"]
        additional_info_bit_1 = parameters.pick_box_action["vertical_correction"]<<1
        definition_full_load = 0
        if parameters.pick_box_action["definition_full_load"]: definition_full_load = (1<<4) + (0<<3) + (1<<2) # 移位后加起来的值，就是开启满载阈值标定的
        additional_info_bit_2_to_4 = (parameters.pick_box_action["load_weigh"]<<2) + definition_full_load
        additional_info_bit_5 = parameters.pick_box_action["check_space"]<<5

        additional_info = additional_info_bit_5 + additional_info_bit_2_to_4 + additional_info_bit_1 + additional_info_bit_0
        finally_state_enum = rf_protocol.ENUM_PICK_BOX_STATES
        wait = parameters.pick_box_action["wait"]

        send_data = self.packet.pick_box_action_package(function_code, command, decoupled_absolute_position, 
                                                        aligned_absolute_position, leave_box_slot_absolute_position, additional_info)
        recv_data = None
        while recv_data not in wait and parameters.stop_signal:
            recv_data = self.udp_data_parse(function_code, send_data)
            parameters.robot_end_state["enum"] = self.robot_state_parse(finally_state_enum, recv_data)
            if recv_data == -1:
                sys.exit(0)

    def pick_pin_action_command(self):
        """pick机器人 pin in  pin out
        """
        function_code = parameters.pick_pin_action["func"]
        cmmand = parameters.pick_pin_action["cmd"]
        finally_state_enum = parameters.pick_pin_action["finally_state_enum"]

        send_data = self.packet.pick_pin_action_package(function_code, cmmand)
        recv_data = self.udp_data_parse(function_code, send_data)
        parameters.robot_end_state["enum"] = self.robot_state_parse(finally_state_enum, recv_data)

    def pick_chain_homing_command(self):
        """pick机器人链条回原点命令
        """
        function_code = parameters.pick_chain_homing["func"]
        command = parameters.pick_chain_homing["cmd"]
        finally_state_enum = parameters.pick_chain_homing["finally_state_enum"]
        wait = parameters.pick_chain_homing["wait"]

        send_data = self.packet.pick_chain_homing_package(function_code, command)
        recv_data = None
        while recv_data not in wait and parameters.stop_signal:
            recv_data = self.udp_data_parse(function_code, send_data)
            parameters.robot_end_state["enum"] = self.robot_state_parse(finally_state_enum, recv_data)
            if recv_data == -1:
                sys.exit(0)

    def pick_sensor_state_command(self):
        """读pick机器人传感器
        """
        function_code = parameters.pick_senson_state["func"]

        send_data = self.packet.pick_sensor_state_package(function_code)
        recv_data = self.udp_data_parse(function_code, send_data)

        if recv_data != rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]:
            homing = recv_data[0] & 0x01
            chain_homing = recv_data[0] & 0x02
            avoidance = recv_data[0] & 0x04
            A1 = recv_data[1] & 0x01
            A2 = recv_data[1] & 0x02
            A3 = recv_data[1] & 0x04
            A4 = recv_data[1] & 0x08
            A5 = recv_data[1] & 0x10
            A6 = recv_data[1] & 0x20
            print(f"homing:{homing}, chain homing:{chain_homing}, avoidance:{avoidance}")
            print(f"A1:{A1}, A2:{A2}, A3:{A3}, A4:{A4}, A5:{A5}, A6:{A6}")
            parameters.pick_senson_state["ret"] = [homing, chain_homing, avoidance, A1, A2, A3, A4, A5, A6]

    def moving_read(self):
        """读机器人位置
        """
        function_code = parameters.moving_read["func"]

        send_data = self.packet.robot_moving_read_package(function_code)
        recv_data = self.udp_data_parse(function_code, send_data)
        print(f"position:{recv_data[0]}, velocity:{recv_data[1]}, torque:{recv_data[2]}")

    def pick_chain_direct_control_command(self):
        """pick机器人链条直接控制
        """
        function_code = parameters.pick_chain_direct_control["func"]
        command = parameters.pick_chain_direct_control["cmd"]
        absolute_target_position = parameters.pick_chain_direct_control["absolute_target_position"]

        send_data = self.packet.pick_chain_direct_control_package(function_code, command, absolute_target_position)
        recv_data = self.udp_data_parse(function_code, send_data)
        while (not abs(absolute_target_position - recv_data[0]) < 100) and parameters.stop_signal:
            recv_data = self.udp_data_parse(function_code, send_data)
            print(f"position:{recv_data[0]}")
            time.sleep(0.0001)

    def robot_halt_action_command(self):
        """机器人急停
        """
        function_code = parameters.halt_action["func"]
        command = parameters.halt_action["cmd"]
        finally_state_enum = parameters.halt_action["finally_state_enum"]
        wait = parameters.halt_action["wait"]

        send_data = self.packet.robot_halt_action_package(function_code, command)
        recv_data = None
        while recv_data not in wait and parameters.stop_signal:
            recv_data = self.udp_data_parse(function_code, send_data)
            parameters.robot_end_state["value"] = self.robot_state_parse(finally_state_enum, recv_data)
            if recv_data == -1:
                sys.exit(0)
        return recv_data

    def pick_sensor_check_command(self):
        """box action sensor check
        """
        function_code = parameters.sensor_check["func"]
        finally_state_enum = parameters.sensor_check["finally_state_enum"]
        wait = parameters.sensor_check["wait"]

        send_data = self.packet.pick_sensor_check_loaded(function_code)
        recv_data = None
        while recv_data not in wait and parameters.stop_signal:
            recv_data = self.udp_data_parse(function_code, send_data)
            parameters.robot_end_state["enum"] = self.robot_state_parse(finally_state_enum, recv_data)
            if recv_data == -1:
                sys.exit(0)
