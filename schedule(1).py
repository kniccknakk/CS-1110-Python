# schedule.py
# na343 and dw483
# Sources/people consulted: NONE
# 2021/05/15
# Skeleton by Prof. Lillian Lee (LJL2), May 5, 2021

"""Defines classes Course, Schedule, StudentSchedule."""


class Schedule:
    """
    An instance represents a set of Courses.

    An instance can represent a course roster.
    So, Courses in this Schedule can overlap in time.

    Instance attributes:

        * name [non-empty str]: the name of this Schedule, e.g.,
            "Cornell Roster Fall 2021" or (for a student schedule) "My Plan A"

        * courses [dictionary with string keys]: maps a course component name,
            like "CS 1110 LEC 001", to a Course object

        * warnings [list of str]: any warnings about this Schedule, such as a
            Course time change

    """

    def __init__(self, n):
        """Initializes a new Schedule with name `n`,
        attribute `courses` to the empty dictionary {},
        and attribute `warnings` set to the empty list.

        Preconditions:
            n: non-empty string.
        """
        self.name = n
        self.courses = {}
        self.warnings = []

    def add(self, c):
        """Adds Course c to this Schedule's `courses` attribute,
        and adds this Schedule to c's list of Schedules it is in.

        Exception: if there is already a Course with the same name as `c`
        scheduled, c is NOT added. But no warning message is produced.

        Precondition: c is a Course object.
        """



        assert isinstance(c, Course),"argument is not a Course but a "+str(type(c))
        pass # STUDENTS: implement this.

        if c.name not in self.courses :
            self.courses[c.name] = c
            c.in_schedules.append(self)




    def getCourseNames(self):
        """Returns a list of the names of the Courses in this Schedule."""
        # Don't depend on the keys of `courses` being correct
        return list(map(lambda c: c.name, self.courses.values()))

    def __str__(self):
        """Returns string representation of this Schedule."""
        out = "Schedule " + self.name + "\n"
        for c in self.courses.values():
            out += c.name + ": " + c.getTime() + "\n"
        out += "Warnings:\n"
        for w in self.warnings:
            out += w + "\n"
        return out

    def __repr__(self):
        # Defined so that printing lists of Schedules looks better
        return self.__str__()

class StudentSchedule(Schedule):
    """
    StudentSchedules do not allow a course to be added if it conflicts
    with a course already in scheduled in it. A warning message is added when
    such an attempt is made.
    """

    # No need for separate __init__ method; just inherit the superclass's exactly.
    # No need for separate __str__ method; just inherit the superclass's exactly.

    def add(self, c):
        """Adds Course c to this Schedule (and adds this Schedule to c's list of
        Schedules).

        Exceptions:
            * if `c` would conflict with a course already in this StudentSchedule,
              `c` is not added, and a warning message of the following form is added to
              this StudentSchedule's `warnings` attribute, for EVERY conflicting
              course:
              "Could not add <c.name> due to conflict with <name of existing course>"

            * if there is already a Course with the same name as `c`
              scheduled, `c` is NOT added. No warning message is added, though.
        Preconditions: c is a Course object.
        """
        assert isinstance(c, Course), "argument is not a Course but a " + str(type(c))
        pass
        # STUDENTS: Finish this implementation below this line, making effective
        # use of super().
        # Do NOT delete this comment block (so the graders can find this easily.)
        # ADD_BLOCK

        error = False

        if c.name not in self.courses :
            for course in self.courses :
                if c.conflictsWith(self.courses[course]) :
                    error = True
                    self.warnings.append("Could not add " + c.name +
                    " due to conflict with " + course)

            if error == False :
                super().add(c)



class Course:
    """ An instance represents a class.

    Instance attributes:
        name [non-empty string]: name of the course
        in_schedules: list of Schedules this Course is in

        # STUDENTS: below this comment block (but within the docstring for class
        # Course), document any attributes you add.
        # Don't delete this comment block, so the graders can easily see what you
        # added.
        #
        # You'll want attribute(s) or method(s) that
        # (1) represent the meeting time of the course,
        # (2) make it easy to retrieve the Course's times in "standard" format
        # (3) make it easy to compute whether another Course conflicts.
        # COURSE_DOCSTRING_BLOCK



    """
    def __init__(self, n, t):
        """
        Creates a new Course with name n, some internal representation of
        meeting time t, and in_schedules set to the empty list

        Preconditions:
            n: non-empty string, no other course of the same name exists.
                (Examples: "CS 1110 LEC 001", "CS 1110 DIS 201")
            t: string of the form (no beginning or trailing spaces)
                <days> <starthrs>:<startms><am or pm>-<endhrs>-<endms><am or pm>
               where <days> is a subsequence of "MTWRF"
               ***OR***
               the string "TBA"

               Examples of valid values for t:
                "MWF 10:10am-2:30pm"
                "R 8:07am-11:00am"
                "TBA"
        """
        self.name = n
        self.in_schedules = []

        # STUDENTS: implement the rest of this method below; leave the lines
        # above alone.
        # Do not delete this comment block, to help the graders find your code.
        # COURSE INIT BLOCK

        self.timedict = {}
        self.timestring = t



        if t != 'TBA' :
            space = t.find(' ')
            date = list(t[:space])
            time = t[space + 1:]

            for x in range(len(date)) :

                day = date[x]
                self.timedict[day] = makelist(time)


        #deal with TBA
        else :
            print("Warning: The time of this course is still TBA")




    def getTime(self):
        """Returns a string form of this Course's time, in the format described
        by the precondition on `t` for method Course.__init__() .
        """
        return self.timestring

        #"getTime not yet implemented" # STUDENTS: Fix this. We start with
                                             # this return value so that our
                                             # code can call your getTime() even
                                             # if you haven't finished it yet.



    def conflictsWith(self, other):
        """Returns True if this Course conflicts with `other`, False otherwise.
        It is not a conflict if one course ends when the other begins.
        Precondition: `other` is a Course object.
        """
        assert isinstance(other, Course), "argument is not a Course but a " + \
            str(type(other))
        #return False # STUDENTS: comment out this line and put your implementation
                     # below this comment block.  Leave the assert statement
                     # alone and at the beginning of your code.
                     # Do not remove this comment block,
                     # so the graders can find where your code starts.
                     # CONFLICTS WITH BLOCK



        if self.timedict == {} or other.timedict =={} :
            return False
            print("unable to determine if there will be a conflict")
            print("this may be because course time has not be decided")

        for x in self.timedict.keys():
            if x not in other.timedict.keys():
                for x in other.timedict.keys():
                    if x not in self.timedict.keys():
                        return False



        for days in self.timedict :
            si = self.timedict[days]

        for days in other.timedict :
            # print(si)
            oi = other.timedict[days]
            #print(oi)
            ss = si[0]
            #print(ss)
            se = si[1]
            #print(se)
            os = oi[0]
            #print(os)
            oe = oi[1]
            #print(oe)



            if se <= os or oe <= ss :
                return False

            if oi == {} or si == {} :
                return False

            else :
                return True



    def changeTime(self, newtime):
        """Alters the time of this course to newtime, unless newtime is the
        same time as this Course already was.

        Also adds a string of the following form to the warnings list of every
        Schedule this Course is listed in:
            <name of this Course>: time changed from <oldtime> to <newtime>
        where oldtime and newtime have a format like "MWF 10:10am-2:30pm".

        Additionally, also adds a itlisted in, *if* newtime
        conflicts with any Course already in the StudentSchedule. (If there
        are multiple conflicts, each conflicting Course should be listed.)
            <name of this Course>: time change causes conflict with <name of
                conflicting course>

        Preconditions: newtime satisfies the same preconditions as `t`
        for method Course.__init__() .
        """
        assert type(newtime) == str, "Argument is not a str but a " + str(type(newtime))
        pass # STUDENTS: implement this


        if self.timestring == newtime :
            return
        else :
            #print("self.timestring")
            for schedule in self.in_schedules :
                schedule.warnings.append(self.name + ": time changed from " \
                + self.timestring + " to " + newtime)

            self.timedict = {}
            self.timestring = newtime


            if self.timestring != 'TBA' :
                space = newtime.find(' ')
                date = newtime[:space]
                time = newtime[space + 1:]

                for x in range(len(date)) :
                    day = date[x]
                    self.timedict[day] = makelist(time)

            for course in schedule.courses.values():
                if self.conflictsWith(course) and course.name != self.name:
                    schedule.warnings.append(self.name \
                    + ": time change causes conflict with " + course.name)

            #deal with TBA
            else :
                print("Warning: The time of this course is still TBA")

    def getScheduleNames(self):
        """Returns a list of the names of the Schedules this Course is in."""
        # Don't depend on the keys of `courses` being correct
        return list(map(lambda s: s.name, self.in_schedules))

    def __str__(self):
        """Returns a two-line string of the form (so includes "\n" in the middle)
            <Course name>: <Meeting Pattern>
            In schedules: <name of sched1>, <name of sched2>, ...
        where <Meeting Pattern> obeys the same formatting conditions as `t` for
        method Course.__init__(). No trailing spaces and the string should not
        end in a comma.

        Exception: If this Course is not in any Schedules, the string returned is:
            <Course name>: <Meeting Pattern>
        """
        return self.name + ": " + self.getTime() + "\nIn schedules: " + \
            ", ".join(self.getScheduleNames())

    def __repr__(self):
        # Defined so that printing lists of courses looks better
        return self.__str__()

# STUDENTS: add any helper functions below this line.
# Do not delete this comment block.
# HELPER FUNCTIONS  BLOCK

def makelist(time):
    """ Create a list that compiles the various times for each day of the week
        represented as minutes after midnight.

        Precondition: times exist for a certain course (and are not TBA)

        Note: example of a time would be 10:10am-2:30pm
    """

    tlist=[]

    middle = time.find('-')
    starting = time[:middle]
    ending = time[middle + 1:]
    starting_val = starting[:-2]
    ending_val= ending[:-2]

    # convert to minutes after midnight

    #start
    start_colon = starting_val.index(':')
    start1_int = int(starting_val[:start_colon])
    start2_int = int(starting_val[start_colon +1:])

    if starting[-2] == 'p' and start1_int != 12 :
        start1_int = (start1_int + 12)*60
    elif starting[-2] == 'a' and start1_int == 12 :
        start1_int = 00
    else :
        start1_int = start1_int*60


    starting = start1_int + start2_int

    tlist.append(starting)

    #end
    # end_colon = ending_val.index(':')
    # end_hours_int = int(ending_val[:end_colon])

    end_colon = ending_val.index(':')
    end1_int = int(ending_val[:end_colon])
    end2_int = int(ending_val[end_colon +1:])

    if ending[-2] == 'p' and end1_int != 12 :
        end1_int = (end1_int + 12)*60
    elif ending[-2] == 'a' and end1_int == 12 :
        end1_int = 00
    else:
        end1_int = (end1_int)*60

    ending = end1_int + end2_int
    tlist.append(ending)
    return tlist

# STUDENTS: add any new classes below this line.
# Do not delete this comment block.
# NEW CLASSES BLOCK


# class Interval:
#     #Attributes: start [integer] and end [integer]
#
#     def __init__(self, s, e):
#
#     #"""interval with start s and end e """
#         self.starting = starting
#         self.ending = ending
#         # self.timedict = course.timedict
#
#     def overlaps(self, other_i):
#         #returns True if this interval starts within other_i"""
#         return other_i.starting <= self.starting < other_i.ending or \
#             self.starting <= other_i.starting < self.ending or \
#             self.starting < other_i.end <= self.ending
#
#     def __str__(self):
#         return "(" + str(self.starting) + ", " + str(self.ending) + ")"



# STUDENTS: this is some quick-and-dirty testing code I wrote up along the way.
# It is meant to inspire you, should you need to make such tests yourself.
# if __name__ == '__main__':
#     import roster_creation
#     initial_courses_to_add = roster_creation.make_initial_course_list()
#     roster = roster_creation.make_sample_roster(initial_courses_to_add)
#     arch1120 = roster.courses["ARCH 1120 STU 520"
#     my_schedule = StudentSchedule("My Plan C")
#     test_courses = [roster.courses["CS 1110 LEC 001"],
#                     roster.courses["AEP 3560 LEC 001"],
#                     roster.courses["FAKER 0000 LEC 002"],
#                     arch1120]
#     for c in test_courses:
#         my_schedule.add(c)

#     arch1120.changeTime("MWF 8:00am-8:00pm")
#     print(arch1120)
#     aep = roster.courses["AEP 3560 LEC 001"]
#
#     < started doing prints of various subcomponents of my Courses to check them>
#     print(my_schedule.warnings)
#     # If got here, did not find any overlapping intervals
#     print("outside")
