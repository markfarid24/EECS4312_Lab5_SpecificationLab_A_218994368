## Student Name: Mark Farid
## Student ID: 218994368

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict, Tuple

def _to_minutes(t: str) -> int:
    hh, mm = t.split(":")
    return int(hh) * 60 + int(mm)

def _to_hhmm(m: int) -> str:
    return f"{m // 60:02d}:{m % 60:02d}"

def _merge(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for s, e in intervals[1:]:
        ps, pe = merged[-1]
        if s <= pe:
            merged[-1] = (ps, max(pe, e))
        else:
            merged.append((s, e))
    return merged

def suggest_slots(events: List[Dict[str, str]], meeting_duration: int, day: str) -> List[str]:
    workStart = _to_minutes("09:00") 
    workEnd = _to_minutes("17:00")
    step = 15 
    intervals: List[Tuple[int, int]] = []
    for ev in events:
        s = _to_minutes(ev["start"])
        e = _to_minutes(ev["end"])
        s = max(s, workStart)
        e = min(e, workEnd)
        if s < e:
            intervals.append((s, e))
    intervals.append((_to_minutes("12:00"), _to_minutes("13:00")))
    busy = _merge(intervals)
    free: List[Tuple[int, int]] = []
    cur = workStart
    for s, e in busy:
        if cur < s:
            free.append((cur, s))
        cur = max(cur, e)
    if cur < workEnd:
        free.append((cur, workEnd))
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
