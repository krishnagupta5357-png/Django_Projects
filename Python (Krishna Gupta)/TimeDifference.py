from datetime import datetime
exam_day = datetime(2026, 1, 25)
now = datetime.now()
remaining = exam_day - now
print("Days Left for Exam:", remaining)