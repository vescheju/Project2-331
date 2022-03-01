"""
PROJECT 2 - Linked List Recursion
Name: Justin Vesche
PID: A56742340
"""


class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = '_value', '_next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self._value = value  # element at the node
        self._next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self._value)

    __str__ = __repr__

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_value(self, value):
        self._value = value

    def set_next(self, next):
        self._next = next


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #


def insert(value, node=None):
    """
    This function inserts a value recursively to end of list
    with base case checking if head is empty. Final
    return always returns head.
    """
    if node is None:
        return LinkedNode(value)
    elif node.get_next() is None:
        node.set_next(LinkedNode(value))
        return node
    insert(value, node.get_next())
    return node


def to_string(node):
    """
    recursively look through each element of list and add to
    a string. If node is empty then empty string is returned.
    """
    node_string = ""
    if node is None:
        return node_string
    node_string = str(node.get_value()) + ', '
    if node.get_next() is not None:
        node_string += to_string(node.get_next())
        if node_string[-2:] == ', ':
            return node_string[:-2]
        return node_string
    else:
        if node_string != '' and node_string[-2:] == ', ':
            return node_string[:-2]
        return node_string


def remove(value, node):
    """
    Base case checks the head node to see if is equal to value, or if
    there is only a head. Else the function recursively checks the list
    and deletes the first element. The lists head is returned.
    """
    if node.get_value() == value:
        node = node.get_next()
        return node
    elif node.get_next() is None:
        return node
    else:
        if node.get_next().get_value() == value:
            node.set_next(node.get_next().get_next())
            return node
        else:
            remove(value, node.get_next())
            return node


def remove_all(value, node):
    """
    Remove all instances of value in list. Uses recursion
    to to change next values of list. Cont. to change
    node if it is equal to value.
    """
    if node is None:
        return node
    if node.get_value() == value:
        node = remove_all(value, node.get_next())
        return node
    else:
        if node.get_value() != value:
            next_node = remove_all(value, node.get_next())
            node.set_next(next_node)
        else:
            return node
    return node


def search(value, node):
    """
    Linearly search list using recursion. Returns true if there, false otherwise.
    """
    if node is None:
        return False
    if node.get_value() == value:
        return True
    elif node.get_next() is None:
        return False
    return search(value, node.get_next())


def length(node):
    """
    Again linearly search the list, updating size accordingly.
    returns the length of the node.
    """
    list_size = 0
    if node is None:
        return list_size
    list_size = 1
    list_size = list_size + length(node.get_next())
    return list_size


def sum_list(node):
    """
    linearly search the list, get its value and add it to list sum.
    If list empty return 0, else return sum
    """
    list_sum = 0
    if node is None:
        return list_sum
    else:
        list_sum += node.get_value() + sum_list(node.get_next())
        return list_sum


def count(value, node):
    """
    linearly search through recursion, updating the value count
    according. Returns 0 if value not in node, else return updated count.
    """
    counted = 0
    if node is None:
        return 0
    if node.get_value() == value:
        counted += 1
        counted += count(value, node.get_next())
    elif node.get_next() is None:
        return 0
    else:
        counted += count(value, node.get_next())
    return counted


def reverse(node):
    """
    use recursion to goto end of the list. Then insert end into a new list
    returning head of that new list.
    """
    if node is None:
        return node
    elif node.get_next() is None:
        return node
    else:
        next_node = reverse(node.get_next())
        next_node = insert(node.get_value(), next_node)
        return next_node


def list_percentage(node, percentage, counter=0):
    """
    use recursion to get to end of list updating counter each time. When end is reached
    check counter and percentage. Return either node or percentage.
    """
    if node is None or percentage == 0:
        return None
    elif percentage == 1:
        return node
    elif node.get_next() is None:
        return node
    else:
        counter += 1
        checker = list_percentage(node.get_next(), percentage, counter)
        if isinstance(checker, int):
            if checker == 1:
                return node.get_next()
            elif checker > 1:
                checker -= 1
                return checker
        else:
            counter = round((counter + 1) * percentage)
            if counter == 1:
                return checker
            elif counter > 1 and checker.get_next() is None:
                counter -= 1
                return counter
    return checker
