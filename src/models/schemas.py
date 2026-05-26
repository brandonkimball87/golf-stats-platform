from enum import Enum
from pydantic import BaseModel

class GolfClub(str, Enum):
    DRIVER = 'Driver'
    TWO_HYBRID = '2-hybrid'
    THREE_HYBRID = '3-hybrid'
    FOUR_HYBRID = '4-hybrid'
    FIVE_IRON = '5-iron'
    SIX_IRON = '6-iron'
    SEVEN_IRON = '7-iron'
    EIGHT_IRON = '8-iron'
    NINE_IRON = '9-iron'
    PITCHING_WEDGE = 'pitching-wedge'
    GAP_WEDGE = 'gap-wedge'

class ShotAccuracy(str, Enum):
    CENTER = 'center'
    RIGHT = 'right'
    LEFT = 'left'
    LONG = 'long'
    SHORT = 'short'

class ShotInput(BaseModel):
    club: GolfClub
    target_distance: int
    actual_distance: int
    accuracy: ShotAccuracy