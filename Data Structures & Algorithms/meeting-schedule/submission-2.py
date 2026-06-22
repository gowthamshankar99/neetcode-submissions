"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    @staticmethod
    def sort_function(val):
        return val.start
            
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
            end of previous needs to be less than start of next 
        """



        if len(intervals) == 0 or len(intervals) == 1:
            return True
        ## sort it first
        intervals.sort(key=self.sort_function)

        previous_start = intervals[0].start
        previous_end = intervals[0].end

        for i in range(1, len(intervals)):
            current_start = intervals[i].start
            current_end = intervals[i].end
            if previous_end > current_start:
                return False
            else:
                previous_end = current_end

        return True


        

