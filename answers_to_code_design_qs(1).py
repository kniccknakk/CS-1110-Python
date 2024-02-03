# answers_to_code_design_qs.py
# na323; dw483
# Sources/people consulted: NONE
# 2021/05/05
# Skeleton by Prof. Lillian Lee (LJL2), Apr 27, 2021


# STUDENTS
# Please make sure your lines are <= 80 characters long.


#### Q1 ####
# In file college_a5.py, are there any advantages to changing `add_student` and
# `was_accepted`, which were non-method functions in A3, into methods of
# class College?
#
# * If so, explain what the advantages are.
#
# * If not, explain why it makes no difference or is even detrimental to
#   switch these non-method functions to methods.
#
# Note; answers that don't mention the specific class College are likely to
# be too vague.
#
'''
#### A1 ####
# STUDENTS: put your answer within these triple quotes.
# A paragraph of 1-4 sentences should suffice

There are advantages to changing `add_student` and `was_accepted` into methods 
of class college. Fundamentally, this change secures the information that these 
functions deal with. If an attacker wanted to change someone's acceptance at a
 college they would simply have to change one function. Adding this function to 
a class would make it more secure since you can add preconditions. For example, 
College.add_student uses class methods so an attacker would have to change 
values of the class rather than just an empty list, which requires specific 
functions of the class. You cannot simply append yourself to a list, such as
 college.accepted, you need to go through the class function `add_student`. 




'''

#### Q2 ####
# Is there any function in sd_utilities_list.py that would be better to
# convert to a method of class Showdown or College?
#
# * If so, name one and explain why it would be advantageous to convert
#   to a method.
#
# * If not, name one and explain why it would make no difference or even
#   be detrimental to switch it to a method.
'''
#### A2 ####
# STUDENTS: put your answer within these triple quotes.
# A paragraph of 1-4 sentences should suffice

The functions in the sd_utilities_list.py would be better to remain as functions 
rather than methods. Those functions typically are not acting on a "self" like 
the functions that are contained in class showdown and college, and rather are
 working on seperate lists of data. For example, in the function college_named,
 a single college is returned from a list of colleges, and there is no specific
 subject in which to call the class College to justify it being part of that 
class. Semantically, it also wouldn't make sense to have 
college.college_named(n) since it would make a lot more sense to just call a 
separate function and get the name from the list. Finally, it wouldn't really
be detrimental to have any of the utility methods as non-class methods
since they don't contain information that can be harmful if seen or modified. 
The functions in the sd_utilities_list.py would be better to remain as functions 
rather than methods. Those functions typically are not acting on a "self" like
 the functions that are contained in class showdown and college, and rather are 
working on seperate lists of data. For example, in the function college_named,
 a single college is returned from a list of colleges, and there is no specific
 subject in which to call the class College to justify it being part of that 
class. Semantically, it also wouldn't make sense to have
 college.college_named(n) since it would make a lot more sense to just call a 
separate function and get the name from the list. Finally, it wouldn't really
be detrimental to have any of the utility methods as non-class methods since
they  don't contain information that can be harmful if seen or modified. 



'''
#### Q3 ####
# Is there any advantage to converting the for-loop in
# sd_utilities_list.college_named() to be a while-loop that can terminate early?
'''
#### A3 ####
# STUDENTS: put your answer within these triple quotes.
# A paragraph of 1-4 sentences should suffice.

It's better to use a while-loop because it can execute the function more
efficiently. Previously, the function interated through the entire clist and
only ends when it gets through each item. Since we now have: while
(found_scname == False), we can stop looking at each item in the list and the
functions  will end once it finds the college name. Additionally, we only need
to iterate once rather than through every college for "enrollment" since each
person only enrolls into one college, and the loop only needs to go through once.
In terms of advantage it pretty much runs and performs the same thing, but we
can spend less time waiting for the code to run, which, while not that
noticeable here, would make a difference if there was a larger dataset.



'''
