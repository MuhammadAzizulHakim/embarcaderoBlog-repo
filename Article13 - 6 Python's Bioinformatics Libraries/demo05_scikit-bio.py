from skbio import DNA, TabularMSA

seqs = [
    DNA('ACGT'),
    DNA('AG-T'),
    DNA('-C-T')
]

msa = TabularMSA(seqs)
print(msa)