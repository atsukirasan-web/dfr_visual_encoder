import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_ON_PRESS, CONF_ON_LONG_PRESS, CONF_ON_CLOCKWISE, CONF_ON_COUNTER_CLOCKWISE
from esphome.cpp_generator import Pvariable, add
from esphome.core import Lambda
from esphome.components import sensor, binary_sensor
from esphome.cpp_types import Component, gpio, i2c

DEPENDENCIES = ["i2c"]

dfrobot_visual_encoder_ns = esphome.codegen.namespace('dfrobot_visual_encoder')
DFRobotVisualEncoder = dfrobot_visual_encoder_ns.class_(
    'DFRobotVisualEncoder', Component, i2c.I2CDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(DFRobotVisualEncoder),
    cv.Optional(CONF_ON_CLOCKWISE): cv.single_automation(),
    cv.Optional(CONF_ON_COUNTER_CLOCKWISE): cv.single_automation(),
    cv.Optional(CONF_ON_PRESS): cv.single_automation(),
    cv.Optional(CONF_ON_LONG_PRESS): cv.single_automation(),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = Pvariable(config[CONF_ID], 0x36)  # default I2C address
    add(var)

    if CONF_ON_CLOCKWISE in config:
        automation = config[CONF_ON_CLOCKWISE]
        for call in automation:
            var.add_on_clockwise_callback(call)
    if CONF_ON_COUNTER_CLOCKWISE in config:
        automation = config[CONF_ON_COUNTER_CLOCKWISE]
        for call in automation:
            var.add_on_counter_clockwise_callback(call)
    if CONF_ON_PRESS in config:
        automation = config[CONF_ON_PRESS]
        for call in automation:
            var.add_on_press_callback(call)
    if CONF_ON_LONG_PRESS in config:
        automation = config[CONF_ON_LONG_PRESS]
        for call in automation:
            var.add_on_long_press_callback(call)