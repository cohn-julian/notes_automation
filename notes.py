"""
Tool for generating and using notes
Goals: 
    Generate new note for each day
    Scheduling template that can be scrapped
    Goals template that can be scrapped
    Analytics dashboard on above
    Logging on words / day 
"""
import sys
from datetime import datetime
from dataclasses import dataclass
from typing import List

class ScheduleItem:
    def __init__(self, start: datetime = None,
                 end: datetime = None, item: str = None
    ):
        self.start = start if start else datetime.now()
        self.end = end
        self.item = item
        
    def __repr__(self):
        pass


class HabitItem:
    def __init__(self, item: str = None, status: bool = False):
        self.item = item
        self.status = status
        
    def __repr__(self):
        pass
    

class Note():
    def __init__(self, start: datetime = None, 
                schedule: List[ScheduleItem] = None, 
                habits: List[HabitItem] = None,
                text: str = None
    ):
        self.start = start if start else datetime.now()
        self.schedule = schedule if schedule else []
        self.habits = habits if habits else []
        self.text = text if text else ""
        
    def __repr__(sef):
        pass
        
    def decode():
        pass
    
