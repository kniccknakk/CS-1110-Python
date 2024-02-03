# a4.py
# na323, dw483
# Sources/people consulted: NONE
# 20210416
# Skeleton by Prof. Lillian Lee (LJL2), Apr 2021

# STUDENTS: do not change the import statement(s) --- our grading framework
# is assuming the same form
import post as post_mod


def num_user_posts(post, u):
    """Returns: The number of Posts whose listed author is u, from among all
    Posts "reachable" from `post` via `replies` attributes.
    The "reachable" Posts are:
        * the Post `post` itself
        * the Posts in post.replies
        * the Posts in the replies list of the Posts in post.replies ... and so on.

    Precondition:
        post: a Post object.
        u: a non-empty string (meant to be a username).
    """

    # STUDENTS: leave these assert statements here. They help prevent recursion
    #           errors where calls are given unexpected argument types.
    assert isinstance(post, post_mod.Post), _type_help("post", 1, "Post")+str(type(post))
    assert isinstance(u, str), _type_help("u", 2, "str")+str(type(u))
    assert len(u) > 0, "2nd argument violates preconditions: "

    # STUDENTS: Complete the implementation, making effective use of recursion.

    accum = 0

    if post.author == u :
        accum = 1
    else :
        accum = 0

    for x in post.replies :
        accum += num_user_posts(x,u)

    return accum





def user_paths(post):
    """Returns: list of strings, one for each reply-path starting from `post`
    and going all the way down to a leaf post (one with no replies to it).
    Each string is a comma-separated sequence of authors along the path, in order.

    If `post` has no replies, the only string to be included is the one
    containing only the author of `post`.

    Preconditions: `post` is a Post object.
    """

    # STUDENTS: leave these assert statements here. They help prevent recursion
    #           errors where calls are given unexpected argument types.
    assert isinstance(post, post_mod.Post), _type_help("post", 1, "Post")+str(type(post))

    # STUDENTS: Complete this implementation, making effective use of recursion.

    if post.replies == [] :
        newlist = [post.author]
        return newlist
    else :
        newlist = []
        for x in post.replies :
            paths = user_paths(x)
            for path in paths :
                path = post.author + ', ' + path
                newlist.append(path)
        return newlist



def bnf_starts_here(post, u1, u2, k):
    """If, ignoring the parent of `post`, a back-and-forth of length k (and not
    longer) between users u1 and u2 starts at Post `post`,
    returns a list of Post objects in that back-and-forth, in top-down order.
    (If there is more than one such back-and-forth, this function returns one of
    them.)

    Otherwise, returns False.

    Preconditions:
        post: a Post object.
        u1 and u2: usernames: non-empty strings that are distinct.
        k: int >= 1."""

    # STUDENTS: leave these assert statements here. They help prevent recursion
    #           errors where calls are given unexpected argument types.
    assert isinstance(post, post_mod.Post), _type_help("post", 1, "Post")+str(type(post))
    assert isinstance(u1, str), _type_help("u1", 2, "str")+str(type(u1))
    assert isinstance(u2, str), _type_help("u2", 3, "str")+str(type(u2))
    assert isinstance(k, int), _type_help("k", 4, "int")+str(type(k))
    assert len(u1) > 0 and len(u2) > 0 and u1 != u2, \
        "u1 and/or u2 violate preconditions"
    assert k >= 1, "k violates preconditions"

    # STUDENTS: Complete this implementation, making effective use of recursion.

    if post.author == u1 :
        if k == 1 and post.replies == [] :
            return [post]
        elif k == 1 and len(post.replies) >= 1 :
            for x in post.replies :
                if x.author == u2 :
                    return False

            return [post]

        elif k > 1 :
            for x in post.replies :
                if x.author == u2 :
                    bnf_starts_here(x, u2, u1, k-1)
                    new_bnf = bnf_starts_here(x, u2, u1, k-1)
                    if type(new_bnf) == list :
                        return [post] + new_bnf
        return False
    else:
        return False


# Helper function for reporting type mismatches for arguments
def _type_help(parname, argpos, partype):
    """Returns 'Arg <argpos>, for parameter <parname>, should have type <partype>,
       but has type '.

    Precondition: parname, partype should be strings. parpos should be an int.
    """

    out =  "Arg " + str(argpos) + ", for parameter" + parname + ", should have"
    out += " type " + partype + ", but has type "
    return out
