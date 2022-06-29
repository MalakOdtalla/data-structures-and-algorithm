from stack_queue_brackets import validation

def test_one():
    stack = validation()
    str='{()[]}'
    actual = stack.validate_brackets(str)
    expected = True
    assert actual == expected

def test_two():
    stack = validation()
    str="{(})"
    actual = stack.validate_brackets(str)
    expected = False
    assert actual == expected