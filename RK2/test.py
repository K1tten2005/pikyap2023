import unittest
from main import *


class TestComputer(unittest.TestCase):
    def test_computer_creation(self):
        computer = Computer(1, "Lenovo", 2077, 1)
        self.assertEqual(computer.id, 1)
        self.assertEqual(computer.name, "Lenovo")
        self.assertEqual(computer.year, 2077)
        self.assertEqual(computer.classroom_id, 1)


class TestClassroom(unittest.TestCase):
    def test_classroom_creation(self):
        classroom = Classroom(1, "254л")
        self.assertEqual(classroom.id, 1)
        self.assertEqual(classroom.classroom_number, "254л")


class TestClassroomsComputers(unittest.TestCase):
    def test_classrooms_computers_creation(self):
        classrooms_computers = ClassroomsComputers(1, 1)
        self.assertEqual(classrooms_computers.computer_id, 1)
        self.assertEqual(classrooms_computers.classroom_id, 1)


class TestTaskExecution(unittest.TestCase):
    def setUp(self):
        self.computer_classrooms, self.computers, self.classrooms_computers = generate_data()

    # Тестирование запроса №1
    def test_task1(self):
        result = task1(self.computer_classrooms, self.computers)
        self.assertEqual(result, [("Lenovo", "254л"), ("Cisco", "254л"), ("Lenovo", "306э"), ("Cisco", "306э")])

    # Тестирование запроса №2
    def test_task2(self):
        result = task2(self.computer_classrooms, self.computers)
        self.assertEqual(result, [("362", 2017), ("253л", 2019), ("306э", 2019), ("107л", 2020), ("254л", 2021)])

    # Тестирование запроса №3
    def test_task3(self):
        result = task3(self.computer_classrooms, self.computers, self.classrooms_computers)
        self.assertEqual(result,
                         {'254л': ['Lenovo', 'Cisco'], '253л': ['Acer']})


if __name__ == "__main__":
    unittest.main()