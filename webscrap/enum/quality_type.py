from enum import Enum

class QualityType(Enum):
    _480P = '480p'
    _720P = '720p'
    _1080P = '1080p'
    _2160P = '2160p'
    _3D = '3D'

class QualityName(Enum):
    BLURAY = 'BluRay'
    WEB = 'WEB'