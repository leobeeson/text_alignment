from Bio import pairwise2
from Bio.pairwise2 import format_alignment

string1 = "if you manage to do them I will tell several friends to follow you"
string2 = "if you manage to make them several of my friends will follow you"

alignments = pairwise2.align.globalxx(string1.split(), 
                                      string2.split(),
                                      gap_char=['-']
                                     )

format_alignment(*alignments[0])

alignments[0][1]


