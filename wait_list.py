from enum import Enum
from rf_protocol import rf_protocol

class wait_list:
    homing = {
        0x00: [
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_IDLE.value["value"], 
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED.value["value"], 
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED_LIFTER_C.value["value"], 
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED_LIFTER_D.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ], 
        0x01: [
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_IDLE.value["value"], 
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ], 
        0x02: [
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED_LIFTER_C.value["value"], 
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED_LIFTER_D.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ], 
        0x03: [
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED_LIFTER_C.value["value"], 
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED_LIFTER_D.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ], 
        0x04: [
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_IDLE.value["value"], 
            rf_protocol.ENUM_HOMING_STATE.HOMING_STATE_COMPLETED.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ]
    }
    
    pick_box_action = {
        0x80: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_NO_BOX.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOADED.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOADING.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_RETURNING.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_UNKNOWN.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_CENTERED.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABLE.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOAD_FAIL.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_UNLOAD_FAIL.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOAD_OVERWEIGHT.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_CHANGE_CLAW_SIDE_COMPLETED.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_CHANGE_CLAW_SIDE_FAIL.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABLE_GRAB_FAIL.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABEL_CHAIN_TORQUE_EXCESS.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_UNLOADED_AT_ENTRANCE.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_CHAIN_POSITION_RECOVER_ERROR.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # LOAD_FROM_A, LOAD_FROM_B, DOUBLE_STORAGE_LOAD_FROM_A, DOUBLE_STORAGE_LOAD_FROM_B
        # fit "0x81", "0x82", "0x85", "0x86"
        0x81: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOADED.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_UNKNOWN.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABLE.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOAD_FAIL.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOAD_OVERWEIGHT.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABLE_GRAB_FAIL.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # UNLOAD_TO_A, UNLOAD_TO_B, DOUBLE_STORAGE_UNLOAD_TO_A, DOUBLE_STORAGE_UNLOAD_TO_B
        # fit "0x83", "0x84", "0x87", "0x88"
        0x83: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_NO_BOX.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_UNKNOWN.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABLE.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_UNLOAD_FAIL.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABLE_GRAB_FAIL.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_UNLOADED_AT_ENTRANCE.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABLE_TRAY_CONNECT_FAIL.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABEL_CHAIN_TORQUE_EXCESS.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_UNLOADED_AT_ENTRANCE.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # LOADED_TO_CENTER
        0x89: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_CENTERED.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # CENTER_TO_LOADED
        0x8A: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOADED.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # RESET_RECOVERABLE_ERROR
        0x8B: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOADED.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_NO_BOX.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # RESET_LOAD_UNLOAD_ERROR
        0x8C: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_NO_BOX.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_CLAW_BREAKDOWN.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # CLAW_SIDE_TO_A, CLAW_SIDE_TO_B
        # fit "0x8D", "0x8E"
        0x8D: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_RECOVERABLE.value["value"], 
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_CHANGE_CLAW_SIDE_COMPLETED.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_CHANGE_CLAW_SIDE_FAIL.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # CLAW_SIDE_ACK
        0x8F: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_LOADED.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # POSITION_RECOVER
        0x90: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_NO_BOX.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_CHAIN_POSITION_RECOVER_ERROR.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # RECOVER_CHAIN_BREAKDOWN
        0x91: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_NO_BOX.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_CANT_RECOVER_FAIL.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        0x92: [
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_NO_BOX.value["value"],
            rf_protocol.ENUM_PICK_BOX_STATES.PICK_BOX_ERROR_CHAIN_BREAKDOWN.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ]
    }
    
    pick_pin_action = {
         0x60: [
            rf_protocol.ENUM_PICK_PIN_STATES.PICK_PIN_IN.value["value"], 
            rf_protocol.ENUM_PICK_PIN_STATES.PICK_PIN_FAIL.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ], 
        0x61: [
            rf_protocol.ENUM_PICK_PIN_STATES.PICK_PIN_OUT.value["value"], 
            rf_protocol.ENUM_PICK_PIN_STATES.PICK_PIN_FAIL.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ]
    }

    pick_chain_homing = {
        0x00: [
            rf_protocol.ENUM_PICK_CHAIN_HOMING_STATES.PICK_CHAIN_HOMING_UNKNOWN.value["value"], 
            rf_protocol.ENUM_PICK_CHAIN_HOMING_STATES.PICK_CHAIN_HOMING_IN_PROGRESS.value["value"], 
            rf_protocol.ENUM_PICK_CHAIN_HOMING_STATES.PICK_CHAIN_HOMING_COMPLETED.value["value"], 
            rf_protocol.ENUM_PICK_CHAIN_HOMING_STATES.PICK_CHAIN_HOMING_ERROR.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ], 
        0x01: [
            rf_protocol.ENUM_PICK_CHAIN_HOMING_STATES.PICK_CHAIN_HOMING_COMPLETED.value["value"], 
            rf_protocol.ENUM_PICK_CHAIN_HOMING_STATES.PICK_CHAIN_HOMING_ERROR.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ], 
        0x02: [
            rf_protocol.ENUM_PICK_CHAIN_HOMING_STATES.PICK_CHAIN_HOMING_UNKNOWN.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ], 
        0x03: [
            rf_protocol.ENUM_PICK_CHAIN_HOMING_STATES.PICK_CHAIN_HOMING_COMPLETED.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ]
    }

    halt_atcion = {
        0x00: [
            rf_protocol.ENUM_HALT_STATE.HALT_STATE_RUNNING.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        0x01: [
            rf_protocol.ENUM_HALT_STATE.HALT_STATE_HALT.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ]
    }

    sensor_check = [
        rf_protocol.ENUM_PICK_SENSOR_CHECK_LOAD_STATES.PICK_SENSOR_LOAD_STATE_OK.value["value"],
        rf_protocol.ENUM_PICK_SENSOR_CHECK_LOAD_STATES.PICK_SENSOR_LOAD_STATE_POSITION_ERROR.value["value"],
        rf_protocol.ENUM_PICK_SENSOR_CHECK_LOAD_STATES.PICK_SENSOR_LOAD_STATE_ERROR.value["value"],
        rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
    ]

    sort_action = {
        # READ_STATE
        0x00: [
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_BUSY.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOADING.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOADED.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOADING.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOADED.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_TIMEOUT_WITHOUT_CARGO.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_TIMEOUT_WITH_CARGO.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_OVERLENGTH.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_TIMEOUT_WITHOUT_CARGO.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_TIMEOUT_WITH_CARGO.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_UNKNOW_PROFILE.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_UNKNOW_PROFILE.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_SENSOR_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_TIME_MOTOR_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_TIME_MOTOR_ERROR.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # # LOAD_FROM_A, LOAD_FROM_B
        # fit "0x01", "0x02"
        0x01: [
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_BUSY.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOADED.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_TIMEOUT_WITHOUT_CARGO.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_TIMEOUT_WITH_CARGO.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_OVERLENGTH.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_UNKNOW_PROFILE.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_SENSOR_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_TIME_MOTOR_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_TIME_MOTOR_ERROR.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
        # UNLOAD_TO_A, UNLOAD_TO_B
        # fit "0x05", "0x06"
        0x05: [
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_BUSY.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOADED.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_TIMEOUT_WITHOUT_CARGO.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_TIMEOUT_WITH_CARGO.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_UNKNOW_PROFILE.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_LOAD_TIME_MOTOR_ERROR.value["value"],
            rf_protocol.ENUM_SORT_ACTION_STATE.SORT_ACTION_STATE_UNLOAD_TIME_MOTOR_ERROR.value["value"],
            rf_protocol.ENUM_TIME_OUT.RECV_DATA_TIME_OUT.value["value"]
        ],
    }
