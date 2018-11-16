def min_by_key(key, records):
    # write your code


def first_by_key(key, direction, records):
    # write your code


class RecordComparator:
    def __init__(self, key, direction):
        # write your code

    def compare(self, a, b):
        # write your code

def test_min_by_key():
    assert min_by_key("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
    assert min_by_key("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
    assert min_by_key("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
    assert min_by_key("a", [{}]) == {}
    assert min_by_key("b", [{"a": -1}, {"b": -1}]) == {"b": -1}
    print("test_min_by_key all passed!")


def test_first_by_key():
    assert first_by_key("a", "asc", [{"a": 1}]) == {"a": 1}
    assert first_by_key(
        "a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [{"b": 1}, {"b": -2}]
    assert first_by_key(
        "a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
    assert first_by_key(
        "b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
    assert first_by_key(
        "b", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": 1}
    assert first_by_key("a", "desc", [
                        {}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]) == {"a": 10, "b": -10}
    print("test_first_by_key all passed!")


def test_comparator():
    cmp = RecordComparator("a", "asc")
    assert cmp.compare({"a": 1}, {"a": 2}) == -1
    assert cmp.compare({"a": 2}, {"a": 1}) == 1
    assert cmp.compare({"a": 1}, {"a": 1}) == 0
    assert cmp.compare({"a": 1}, {"b": 1}) == 1

    cmp2 = RecordComparator("a", "desc")
    assert cmp2.compare({"a": 1}, {"a": 2}) == 1
    assert cmp2.compare({"a": 2}, {"a": 1}) == -1
    assert cmp2.compare({"a": 1}, {"a": 1}) == 0
    assert cmp2.compare({"a": 1}, {"b": 1}) == -1
    print("test_comparator all passed!")


test_min_by_key()
test_first_by_key()
test_comparator()
