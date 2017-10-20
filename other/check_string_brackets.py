
def check_string_brackets(string):
    """ return True if all brackets in string has a pair (open and close)
        otherwise False
    """
    # set tuple for open and closed chars
    # index used for set a pair open and closed
    openchars = ('{', '(',)
    closechars = ('}', ')',)
    # set zero element None
    opened = [None]

    for char in string:
        if char in openchars:
            # add new open index to targets
            opened.append(openchars.index(char))
        elif char in closechars:
            if opened[-1] == closechars.index(char):
                # if closed and open index are equal
                # delete last target index
                del opened[-1]
            else:
                return False
    if opened == [None]:
        # if opened indexes are the same
        return True
    return False

if __name__ in "__main__":
    for correct, item in [(True, '{hello()}'),
                          (False, '{hello(}'),
                          (True, '{hello()()hshsh(jsjsj())}'),
                          (False, '}hello()()hshsh(jsjsj())}'),
                          (True, ''),
                          (False, '{'),
                          (False, '}'),]:
        print(correct == check_string_brackets(item), item)
