## Student Name: Mark Farid
## Student ID: 218994368

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict, Tuple

def suggest_slots(events: List[Dict[str, str]], meeting_duration: int, day: str) -> List[str]:
    work_start = _to_minutes("09:00") 
    work_end = _to_minutes("17:00")
    step = 30 
    intervals: List[Tuple[int, int]] = []
    for ev in events:
        s = _to_minutes(ev["start"])
        e = _to_minutes(ev["end"])
        s = max(s, work_start)
        e = min(e, work_end)
        if s < e:
            intervals.append((s, e))
    busy = _merge(intervals)
    free: List[Tuple[int, int]] = []
    cur = work_start
    for s, e in busy:
        if cur < s:
            free.append((cur, s))
        cur = max(cur, e)
    if cur < work_end:
        free.append((cur, work_end))
    out: List[str] = []
    for gs, ge in free:
        latest = ge - meeting_duration
        if latest < gs:
            continue
        t = gs
        while t <= latest:
            out.append(_to_hhmm(t))
            t += step
    return out
