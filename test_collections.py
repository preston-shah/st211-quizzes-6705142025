def test_list_equality():
    assert [1, 2, 3] == [1, 2, 3]

    def test_list_contents():
        result = [3, 1, 2]    
        assert sorted(result) == [1, 2, 3]

    def test_dict_equality():
        expected = {"name": "Alice", "age": 30}
        actual = {"age": 30, "name": "Alice"}
        assert actual == expected   

    def test_set_operations():
        assert {1, 2, 3} & {2,3, 4} == {2,3}