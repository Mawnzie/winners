from winners import parse_csv

import unittest
import pandas as pd
import os

class Tests(unittest.TestCase):
    path = os.getcwd() + "/csv_files_for_testing/"

    #Test that the percentage output works as expected:
    def test_increment(self):
        self.assertEqual(float(parse_csv(Tests.path+"TestIncrement.csv")['percent'][0][:-1]),0.23)
        self.assertEqual(float(parse_csv(Tests.path +"TestIncrement.csv")['percent'][1][:-1]),-1.63)

    #Test that correct exception is thrown when a csv-file with no values is passed:
    def test_empty_dataframe(self):
        self.assertRaises(Exception,parse_csv,Tests.path+"novals.csv")
    
    #Test exception when the csv-file is empty:
    def test_emptyfile(self):
        self.assertRaises(pd.errors.EmptyDataError,parse_csv,Tests.path +"empty.csv")
    
    #Check that corrupted values in date column raises exception
    def test_corrupted_date(self):
        self.assertRaises(ValueError,parse_csv,Tests.path +"corrupted_date.csv")
        
    #Check that corrupted values in date column raises exception
    def test_corrupted_value(self):
        self.assertRaises(Exception,parse_csv,Tests.path+"corrupted_kurs.csv")
        

if __name__ == "__main__":
    unittest.main()
