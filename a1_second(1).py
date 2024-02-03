# a1_second.py
# na323
# NONE
# 20210304
# Skeleton by Prof. Lee (cs1110-prof@cornell.edu), Feb 25 2021

"""
Functions for the modality and open/closed/waitlist status of a class component
according to a class roster webpage.

"""


def make_url(part1, part2, part3):
    """Returns: new string of the form part1/part2/part3

    Preconditions: part1, part2, and part3 are all nonempty strings.

    The intent, although not a precondition, is:
        part1 is like "https://classes.cornell.edu/browse/roster/SP21/class"
        part2 is like "CS"
        part3 is like "1110"
    and the returned string would be
        https://classes.cornell.edu/browse/roster/SP21/class/CS/1110
    """

    url = part1 + '/'+  part2 + '/'+ part3


    return url


def tag_endi(tag, text):
    """Returns: the index of the end of the first occurrence of `tag` in `text`

    Preconditions:
        `text` [str]: contains at least one instance of `tag`
        `tag`  [str]: length > 0

    Examples:
        tag_endi("+", "ab+c") --> 2
        tag_endi('<name "intro">','faith <name "intro"> hope charity') --> 19
    """

    endnum = text.index(tag)+((len(tag))-1)


    return endnum


def from_to(start, end, text):
    """Returns substring of `text` occurring between the 1st occurrence of
    `start` and the first following occurrence of `end`.

    Preconditions:
    `text` [str]: length > 0.
    `start` and `end` [str]: both non-empty and occur in `text`.
    At least one `end` appears after a `start` in `text`.

    Examples:
    from_to('+', '!', '+a+b+c!+4def+5') ---> 'a+b+c'
    from_to('(', ')', 'good job :) good example foo(0) ') --> '0'
    t = '<li style="color:purple">python</li><span>the < is intentional</span>'
    from_to('<span>','</span>', t') ---> "the < is intentional"
    """


    starting = (tag_endi(start,text)+1)


    inside = text[ starting : text.index(end, starting)]


    return inside



def report_section(s):
    """Returns string of the form
        '<component type> <section number> <open status> <mode>'.
    The component type, mode, and open status should have the first letter
    capitalized, and all other letters lower-case.  The section number should be
    exactly as in s with respect to capitalization, spacing, and so on.

    See a1_first.test_report_section() for examples.

    Preconditions:
    `s` is a string of the following form, where CT, SN, OS, and MODE
    indicates word(s) without quotation marks or angle brackets ("<" or ">"),
    and "..." stands for anything:

        ...data-ssr-component="CT" ... data-section="SN" ...
        open-status-OS" ... class="instr-mode">Instruction Mode: MODE</span> ...

    BUT where the following substrings occur exactly once:
        'data-ssr-component="'
        'data-section="'
        'open-status-'
        'class="instr-mode">Instruction Mode:'
    """


    CT = from_to('data-ssr-component="','"', s)
    SN = from_to( 'data-section="', '"', s)
    OS = from_to('open-status-', '"',s )
    MODE = from_to('class="instr-mode">Instruction Mode: ', '<',s)


    status = (CT.capitalize() + ' ' + SN + ' ' + OS.capitalize() + ' ' + \
    MODE.capitalize())

    
    return status
