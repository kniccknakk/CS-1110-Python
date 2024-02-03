# explanation_of_time_handling.py
# na323 and dw483
# Sources/people consulted: NONE
# 2021/05/15
# Skeleton by Prof. Lillian Lee (LJL2), May 2021


# STUDENTS:
# Explain below, within the triple-quotes, your ideas of how to represent
# course times and how to compute whether two courses overlap in time.
# 1-3 paragraphs should suffice. We aren't grading on the quality of your
# writing; rather, we need your explanation in order to be able to understand
# and fairly grade your code.
#
# Please make sure your lines are <= 80 characters long or thereabouts.
#
# Don't forget to explain how you handle "TBA" as a time.

'''

Our idea was to represent the course times as integers as minutes after midnight
In this manner we would be to mathmatically compare these times (expressed as
integers) using inequality symbols.

Furthermore, we would want to create a dictionary in which the days are keys
and the times are definitions; this way we could compare for conflicts on each
day, which is something we certainly would need to do. (After all, a class at
2:30pm on a Thursday doesn't conflict with a class at 2:30pm on a Monday)

Obviously, 'TBA' is a special case which we would want to deal with seperately.
For such situations, we don't necessarily want to mark it as a conflict when we
are comparing it, but rather print some sort of indication saying, "this class
is marked as TBA, we don't know if there is a conflict; proceed with caution."

'''
