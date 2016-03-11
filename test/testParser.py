import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
import unittest
from app.parser import Parser


class TestParser(unittest.TestCase):
    def setUp(self):
        """
        Setup function for all test cases
        :return: NA
        """
        data = Parser('res/test_list.xml', 'res/test_log.xml', False)
        self.svn_log = data.svn_log
        self.svn_list = data.svn_list

    def test_number_directories(self):
        """
        Checking if the number of main project directories match to check if
        parse directories worked
        :return: NA
        """
        self.assertTrue(len(self.svn_list['root']['nodes']) == 3)

    def test_number_files(self):
        """
        Test if the number of files on the subversion matches what the parser returned
        :return: NA
        """
        self.assertTrue(len(self.svn_log) == 89)

    def test_number_versions(self):
        """
        Test to check if the number of versions of a particularly chosen file matches
        :return: NA
        """
        self.assertTrue(len(self.svn_log['/gvndprs2/Assignment1.0/src/test/testBoard.java']) == 9)

    def test_deleted_file(self):
        """
        File /gvndprs2/list3.txt was deleted in one of the versions of svn. In the test_log.xml,
        there is an entry that this file was deleted. This test checks if deleted files are listed
        in svn_list
        :return: NA
        """
        for i, val in enumerate(self.svn_list['root']['nodes']):
            self.assertTrue('list3.txt' not in val['text'])

    def test_multiple_files(self):
        """
        Testing if multiple revisions for multiple files is held correctly by the svn_log dictionary
        :return: NA
        """
        has_1388 = False
        has_1374 = False
        for i, val in enumerate(self.svn_log['/gvndprs2/Assignment1.0/src/code/types/Pawn.java']):
            if val.revision == 1374:
                has_1374 = True
            elif val.revision == 1388:
                has_1388 = True
        self.assertTrue(has_1388 and has_1374)