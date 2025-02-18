def convert_grade(score):
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        raise ValueError("Score must be a number between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


import unittest


class TestGradeConversion(unittest.TestCase):
    def test_A_grade(self):
        self.assertEqual(convert_grade(95), "A")
        self.assertEqual(convert_grade(90), "A")

    def test_B_grade(self):
        self.assertEqual(convert_grade(85), "B")
        self.assertEqual(convert_grade(80), "B")

    def test_C_grade(self):
        self.assertEqual(convert_grade(75), "C")
        self.assertEqual(convert_grade(70), "C")

    def test_D_grade(self):
        self.assertEqual(convert_grade(65), "D")
        self.assertEqual(convert_grade(60), "D")

    def test_F_grade(self):
        self.assertEqual(convert_grade(50), "F")
        self.assertEqual(convert_grade(0), "F")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            convert_grade(-10)
        with self.assertRaises(ValueError):
            convert_grade(110)
        with self.assertRaises(ValueError):
            convert_grade("abc")
        with self.assertRaises(ValueError):
            convert_grade(None)


if __name__ == "__main__":
    unittest.main()
