from Bio.Seq import Seq
from Bio import SeqIO

my_seq = Seq("AGTACACTGGT")

print(my_seq)
print(my_seq.complement())
print(my_seq.reverse_complement())

for seq_record in SeqIO.parse("C:/Users/ASUS/Bio/examples/ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))