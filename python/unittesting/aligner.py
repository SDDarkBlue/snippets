class Aligner():
    def calculateMatrix(self, sequence1, sequence2):
        matrix = []
	sequence1_index = 0
	for nucleotide1 in sequence1:
	    matrix.append([])
	    for nucleotide2 in sequence2:
		if nucleotide1 == nucleotide2:
		    matrix[sequence1_index].append(0)
		else:
		    matrix[sequence1_index].append(1)
	    sequence1_index += 1
	print matrix
	return matrix
