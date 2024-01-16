import unittest


def subarraysum_to_targetvalue(my_list: list, target_value: int) -> list:
    """
        :type strs: List[str]
        :rtype: str
    """
    """WRITE YOUR SOLUTION BELOW"""


"""TESTS ARENA:"""


# TEST ARENA
class TestingSubArraySumToTargetVal(unittest.TestCase):
    def test_none_matching_subarr1(self):
        """ input: list, """
        self.assertEqual(subarr_sum_to_target_val(
            my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=16), [])

    def test_none_matching_subarr2(self):
        self.assertEqual(subarr_sum_to_target_val(
            my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=13), [])

    def test_found_matching_sub_arr1(self):
        self.assertEqual(subarr_sum_to_target_val(
            [8, 4, 5, 0, 3, 2, 1, 6, 7, 9], 6), [3, 6], "✅!")

    def test_found_matching_sub_arr2(self):
        self.assertEqual(subarr_sum_to_target_val(
            [8, 4, 5, 0, 3, 2, 1, 6, 7, 9], 10), [2, 5], "✅!")

    # IF ALL above passed!, activate the ones below:
    # RAINY DAY TESTS:
    # def test_target_arg_is_nonetype(self):
    #     self.assertEqual(subarr_sum_to_target_val(
    #         my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=None), "✅!")

    # def test_list_arg_is_nonetype(self):
    #     self.assertEqual(subarr_sum_to_target_val(
    #         my_list=None, target_value=10), [], "✅!")

    # def test_list_arg_is_empty(self):
    #     self.assertEqual(subarr_sum_to_target_val(
    #         my_list=[], target_value=10), [], "✅!")

    # def test_list_arg_isnot_integer(self):
    #     self.assertEqual(subarr_sum_to_target_val(
    #         my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value="Hello",),  "✅!")


if __name__ == "__main__":
    unittest.main()
