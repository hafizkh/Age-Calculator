import unittest
import ageUtils

class ageTest(unittest.TestCase):
    def test_if_age_less_than_18(self):
       # Arrange
        age = int(15)
        # Act
        result = ageUtils.ageVerification(age)
        # Assert
        self.assertEqual(result,'You are a Child')


    def test_if_age_greater_than_18(self):
       # Arrange
        age = int(65)
        expectedResult = str('You are an Adult')
        # Act
        result = ageUtils.ageVerification(age)
        # Assert
        self.assertEqual(result,expectedResult)
  

    def test_if_age_greater_than_70(self):
       # Arrange
        age = int(98)
        expectedResult = str('You are a Pensioner')
        # Act
        result = ageUtils.ageVerification(age)
        # Assert
        self.assertEqual(result,expectedResult)

if __name__ == "__main__":
    unittest.main()     
