from Bio.Seq import Seq
my_seq = Seq('ATGCATGCATGC')
print(my_seq.complement())

from Bio import SeqIO
for seq_record in SeqIO.parse()