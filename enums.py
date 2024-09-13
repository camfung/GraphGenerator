from enum import Enum, auto


class Columns(Enum):
    SYMBOLING = "symboling"
    MAKE = "make"
    FUEL_TYPE = "fuel-type"
    ASPIRATION = "aspiration"
    NUM_OF_DOORS = "num-of-doors"
    BODY_STYLE = "body-style"
    DRIVE_WHEELS = "drive-wheels"
    ENGINE_LOCATION = "engine-location"
    WHEEL_BASE = "wheel-base"
    LENGTH = "length"
    WIDTH = "width"
    HEIGHT = "height"
    CURB_WEIGHT = "curb-weight"
    ENGINE_TYPE = "engine-type"
    NUM_OF_CYLINDERS = "num-of-cylinders"
    ENGINE_SIZE = "engine-size"
    FUEL_SYSTEM = "fuel-system"
    BORE = "bore"
    STROKE = "stroke"
    COMPRESSION_RATIO = "compression-ratio"
    HORSEPOWER = "horsepower"
    PEAK_RPM = "peak-rpm"
    CITY_MPG = "city-mpg"
    HIGHWAY_MPG = "highway-mpg"
    PRICE = "price"


class GraphType(Enum):
    SCATTER = auto()
    BAR = auto()
    LINE = auto()
    HISTO = auto()
