# sd_utilities_list.py
# na323; dw483
# Sources/people consulted: NONE
# 2021/05/05
# Skeleton by Prof. Lillian Lee (LJL2), Apr 27, 2021

"""
    Utilities for computing showdown info.

    Assumption: inside the directory containing this file, there is a directory
    called "data" that contains college-data files formatted as described in
    the CS1110 Spring 2021 A3 handout.


    Works with lists of colleges (as opposed to dictionaries as in A3)

"""

import college_a5 as college_module
import os

DATADIR="data"


def colleges_from_file(fn):
    """Returns a list of Colleges from file fn, sorted in reverse order of
    number of applications to each college.

    Preconditions:

        fn: nonempty string.  It is the name of a file

        Inside the directory containing this file, there is a directory
        called "data" that contains college-data files formatted as described in
        the CS1110 Spring 2021 A3 handout.

        One of the files in that "data" directory has the name `fn`.

    """
    colleges = []
    with open(os.path.join(DATADIR,fn), "r") as fp:
        for studentline in fp:
            process_line(studentline.strip(), colleges)
    colleges.sort(key=lambda c: len(c.rejected) \
                                + len(c.accepted_not_enrolled) \
                                + len(c.rejected) + \
                                len(c.waitlisted),
                  reverse=True)
    return colleges



# STUDENTS: Rewrite the implementation of this function as follows:
#
# Use one or more while-loops to rewrite the "for c in clist" for-loop,
# where the while-loops don't go through the entire clist unless the name being
# searched for doesn't show up in any College in clist.
#
# For the purpose of practicing while-loops, you may NOT call college_named
# (although doing so leads to more compact code), and you may NOT use
# `break`, `continue`, or similar statements.
#
# If you introduce new variables, give them understandable names and/or
# provide comments that explain their intended type and "meaning."
#
# Leave the first 7 lines or so of code alone --- only make changes below
# the "BELOW THIS LINE" comment.

def process_line(sline, clist):
    """ Add the tag of sline to the appropriate list (accepted_enrolled,
    ..., or waitlist) of each College in clist; if sline names a college
    not already represented in clist, a corresponding College is added
    to clist.

    Preconditions: sline is a string formatted as if it were a line from a data file
    described in the CS1110 Spring 2021 A3 handout.

    sline does not have trailing newlines.

    clist is a list of Colleges, possibly empty."""

    # STUDENTS: leave the following lines alone; only make changes
    # below where indicated

    tag = int(sline[:sline.index(">>")].strip())

    # name of college student enrolled at
    senrolled_cn = sline[sline.rindex(":")+1:].strip()

    outcomes = sline[sline.index(">>") + len(">>"):sline.rindex('##')].split("##")

    for outcome in outcomes:
        oc = outcome.split(":")
        scname= oc[0].strip() # name of a college supplied by student
        decision = oc[1].strip()

        # STUDENTS: ONLY MAKE CHANGES TO process_line BELOW THIS LINE
        found_scname = False # have not found scname in clist yet
        # have not found enrolled yet (for non-college options)
        found_enrolled = False


        i = 0
        while (found_scname == False) and (i < len(clist)) :
            if clist[i].name == scname :
                found_scname = True
                clist[i].add_student(tag, decision, senrolled_cn)
            i = i + 1
        if not found_scname :
            new_c = college_module.College(scname)
            new_c.add_student(tag, decision, senrolled_cn)
            clist.append(new_c)
            if senrolled_cn == scname :
                found_enrolled = True
    i = 0
    while (found_enrolled == False) and (i < len(clist)) :
        if clist[i].name == senrolled_cn :
            found_enrolled = True
        i = i + 1
    # if not found_enrolled :

        # LEAVE THIS COMMENT IN YOUR SUBMITTED CODE.
        # found_scname = False # have not found scname in clist yet
        # found_enrolled = False # have not found enrolled yet
        #(for non-college options)
        # for c in clist:
        #     if c.name == scname:
        #         found_scname = True
        #         # place tag in correct status list for c
        #         c.add_student(tag, decision, senrolled_cn)
        #     if c.name == senrolled_cn:
        # #         found_enrolled = True
        # if not found_scname:
        #     new_c = college_module.College(scname)
        #     new_c.add_student(tag, decision, senrolled_cn)
        #     clist.append(new_c)
        #     if senrolled_cn == scname:
        #         # now the enrolled school is in clist
        #         found_enrolled = True
    if not found_enrolled:
        # apparently "enrolled" in something they didn't apply to, like "gap year"
        new_c = college_module.College(senrolled_cn)
        new_c.add_student(tag, decision, senrolled_cn)
        clist.append(new_c)


def prompt_for_data(datafilename=""):
    """
    Returns: a list of Colleges from datafile determined by querying the user...
    unless a filename is given, in which case data/filename is the data source.


    Precondition: interaction happens in a directory where a folder named "data"
    is located.
    """
    if len(datafilename) > 0:
        return colleges_from_file(datafilename)

    # A dictionary! Keys are strings because input() returns a string.
    response_map = {
        '1': 'small_test1.txt',
        '2': 'small_cornell_and_suny_test.txt',
        '3': 'a2c_census2020_processed.txt',
        'other': 'some other file in the "data" directory'
    }

    msg = "What college-info file in directory \"data\" should I use?\n"
    for r in ['1', '2', '3', 'other']:
        msg += r + ": " + response_map[r] + "\n"
    msg += ("Default is 1.\n")
    response =input(msg + '\nYour choice? ')
    if response not in response_map:
        # Default to '1'.
        response = '1'

    if response == 'other':
        print("\nOK!. The files I know about are: ")
        for name in glob.glob("data/*"):
            print(name[len("data/"):])
        datafilename = input('Which file you would like? ')
    else:
        datafilename = response_map[response]

    # In contrast to A3, this is not wrapped in try-except, so that students
    # can see what errors are raised by process_line.
    return colleges_from_file(datafilename)


def college_named(n, clist):
    """
    Returns the College in clist that has name `n`, or None (not the string, but
    the value None) if there is no such College in clist.

    Precondition: clist is a (potentially empty) list of Colleges. None of the
    items in clist is None.  No more than one College in clist can have the
    name `n`.
    """
    for c in clist:
        if c.name == n:
            return c


def menu_listing(colleges):
    """Returns: string of numbered names of the colleges in `colleges`, starting
    with 0.

    Format for each college:  '0: Whatsamatta_U'
    (so, colon after number, then 1 space.)

    The numbered-name items are separated by a tab (\t).

    Example: for the list colleges_from_file('small_test1.txt'), the output
    is
        '0: B\t1: A\t2: D\t3: E'
    which prints out as
        0: B    1: A    2: D    3: E

    There is no newline ('\n') or whitespace at the end of the returned string.

    Precondition: `colleges` is a list of Colleges (possibly empty.)
    """
    separator = '\t' # in case we later want '\n' instead of '\t' between items
    out = ''
    i = 0
    for c in colleges:
        out += str(i) + ": " + colleges[i].name + separator
        i += 1
    return out.strip()
