import unittest
from main import is_leap_year
# from solution import is_leap_year


# class TestLongestCommonPrefix(unittest.TestCase):

#     def test_basic_functionality(self):
#         self.assertEqual(longest_common_prefix(
#             ["flower", "flow", "flight"]), "fl")
#         self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

#     def test_empty_list(self):
#         self.assertEqual(longest_common_prefix([]), "")

#     def test_single_string(self):
#         self.assertEqual(longest_common_prefix(["alone"]), "alone")

#     def test_no_common_prefix(self):
#         self.assertEqual(longest_common_prefix(["abc", "def", "ghi"]), "")

#     def test_varied_length_strings(self):
#         self.assertEqual(longest_common_prefix(["a", "ab", "abc"]), "a")
#         self.assertEqual(longest_common_prefix(
#             ["longest", "longer", "long"]), "long")

class TestingIsLeapYear(unittest.TestCase):
    def testing_is_leap_year(self):
        year_list = [2000, 2004, 2008, 2012, 2016, 2020,
                     2024, 2028, 2032, 2036, 2040, 2044, 2048]
        self.assertEqual(is_leap_year(year_list), len(year_list))
        year_list = [1900, 1999, 2001, 2002, 2003,
                     2005, 2100, 1800, 2200, 2300, 2500]
        self.assertEqual(is_leap_year(year_list), 0)
        year_list = [year for year in range(2000, 2025)]
        self.assertEqual(is_leap_year(year_list), 7)

if __name__ == "__main__":
    unittest.main()
