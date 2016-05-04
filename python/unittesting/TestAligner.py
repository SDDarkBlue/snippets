#!/usr/bin/python
import sys
import aligner
import unittest

class AlignerTestcase(unittest.TestCase):
    def test_createAligner(self):
	al = aligner.Aligner()
	pass

    def test_simpleMatrix(self):
	al = aligner.Aligner()
	sequence1 = "A"
	sequence2 = "A"
	expected_matrix = [[0]]
	self.assertEqual(al.calculateMatrix(sequence1, sequence2), expected_matrix)

    def test_simpleMatrixTwoNucleotides(self):
	al = aligner.Aligner()
	sequence1 = "AA"
	sequence2 = "AA"
	expected_matrix = [[0, 0], [0, 0]]
	self.assertEqual(al.calculateMatrix(sequence1, sequence2), expected_matrix)

    def test_simpleMatrixDiffNucleotides(self):
	al = aligner.Aligner()
	sequence1 = "AG"
	sequence2 = "AA"
	expected_matrix = [[0, 0], [1, 1]]
	self.assertEqual(al.calculateMatrix(sequence1, sequence2), expected_matrix)


#    def test_alignTwoSequence():
#        al = aligner.Aligner()
#        sequence1 = "A"
#        sequence2 = "A"
#        alignment = "A\n|\nA"
#        assert(al.alignSequences(sequence1, sequence2), alignment)

def suite():
    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromTestCase(AlignerTestcase)
    return testsuite

def test():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testsuite)

test()

