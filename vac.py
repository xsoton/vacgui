from PyQt6.QtCore import Qt, QDateTime
import enum
from dataclasses import dataclass
from typing import List

@enum.unique
class StateEnum(enum.IntEnum):
	new = 1
	in_progress = 2
	done = 3
	stopped = 4

@dataclass
class VacInfo:
	sample: str
	comment: str
	date: QDateTime
	state: StateEnum

@dataclass
class VacCurveParameters:
	channal: int
	start: float
	stop: float
	step: float
	delay: float

@dataclass
class VacCurveDataPoint:
	index: int
	time: float
	V1: float
	I1: float
	V2: float
	I2: float

@dataclass
class VacCurve:
	parameters: VacCurveDataPoint
	data: List

@dataclass
class Vac:
	info: VacInfo
	curves: List
