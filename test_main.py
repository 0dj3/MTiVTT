import unittest
from unittest.mock import patch
from io import StringIO
from classes import institute
from pukpuk import main


class TestMain(unittest.TestCase):
    inst = institute.Institute()
    s = ['ФИИТ']
    s4 = ['Болуодьа Чтото Сделал', 173531]
    s6 = ['ФИИТ', 2017]


    @patch('builtins.input', side_effect=s)
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_output, mock_input):
        main(["", "add", "spec"])
        self.assertEqual(mock_output.getvalue(), 'ФИИТ\n')

    def test_2(self):
        s2 = [73201202]
        with patch('builtins.input', side_effect=s2):
            with self.assertRaises(Exception):
                main(["", "add", "spec"])

    def test_3(self):
        s3 = ['ФИИТ-228']
        with patch('builtins.input', side_effect=s3):
            with self.assertRaises(Exception):
                main(["", "add", "spec"])

    @patch('builtins.input', side_effect=s4)
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_output, mock_input):
        main(["", "add", "stud"])
        self.assertEqual(mock_output.getvalue(), self.s4[0] + '\n')

    def test_5(self):
        s5 = ['abc', '17']
        with patch('builtins.input', side_effect=s5):
            with self.assertRaises(Exception):
                main(["", "add", "stud"])

    @patch('builtins.input', side_effect=s6)
    @patch('sys.stdout', new_callable=StringIO)
    def test_6(self, mock_output, mock_input):
        main(["", "add", "group"])
        self.assertEqual(mock_output.getvalue(), 'ФИИТ-17\n')


if __name__ == '__main__':
    unittest.main()
