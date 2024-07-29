import unittest
from robot import Robot

class TestRobot(unittest.TestCase):

    def setUp(self):
        """Set up a robot instance for testing"""
        self.robot = Robot(name="TestBot")

    def test_initialization(self):
        """Test the initialization of the robot"""
        self.assertEqual(self.robot.name, "TestBot")
        self.assertEqual(self.robot.battery, 100)
        self.assertEqual(self.robot.skills, [])

    def test_charge(self):
        """Test the charge method"""
        self.robot.battery = 50
        self.robot.charge()
        self.assertEqual(self.robot.battery, 100)

    def test_say_name_with_battery(self):
        """Test say_name method when battery is sufficient"""
        result = self.robot.say_name()
        self.assertEqual(result, "BEEP BOOP BEEP BOOP. I AM TESTBOT")
        self.assertEqual(self.robot.battery, 99)

    def test_say_name_with_low_battery(self):
        """Test say_name method when battery is low"""
        self.robot.battery = 0
        result = self.robot.say_name()
        self.assertEqual(result, "Low power. Please charge and try again")

    def test_learn_skills_with_sufficient_battery(self):
        """Test learn_skills method when battery is sufficient"""
        result = self.robot.learn_skills("dancing", 10)
        self.assertEqual(result, "WOAH. I KNOW DANCING")
        self.assertEqual(self.robot.battery, 90)
        self.assertIn("dancing", self.robot.skills)

    def test_learn_skills_with_insufficient_battery(self):
        """Test learn_skills method when battery is insufficient"""
        self.robot.battery = 5
        result = self.robot.learn_skills("dancing", 10)
        self.assertEqual(result, "Insufficient battery. Please charge and try again")
        self.assertEqual(self.robot.battery, 5)
        self.assertNotIn("dancing", self.robot.skills)

if __name__ == '__main__':
    unittest.main()
