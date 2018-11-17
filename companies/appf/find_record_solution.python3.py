def min_by_key(key, records):
    return first_by_key(key, "asc", records)


def first_by_key(key, direction, records):
    if not records:
        return {}

    cmp = RecordComparator(key, direction)
    ans = records[0]
    for record in records[1:]:
        if cmp.compare(record, ans) < 0:
            ans = record

    return ans


class RecordComparator:
    def __init__(self, key, direction):
        self.key = key
        self.direction = direction

    def compare(self, a, b):
        a_value = a.get(self.key, 0)
        b_value = b.get(self.key, 0)

        if a_value < b_value:
            return -1 if self.direction == "asc" else 1
        elif a_value > b_value:
            return 1 if self.direction == "asc" else -1
        return 0


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
