"""
Video: Course 13 – Python Logical Operators
Topic: and, or, not
Timestamp: 12:15
----------------------------------------
-------------- PYTHON TASK --------------
Allow access only if the user is logged in or they are a guest,
but they must not be banned.
----------------------------------------
"""

# -------- My-Solution --------

login=False
guest=True
banned=False
print(not banned and (guest or login))