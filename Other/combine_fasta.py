from Bio import SeqIO

#Change file list to list of fasta files you want to combine
#Example: file_list = ["x.fasta", "y.fasta"] 
#Change output.fasta to name of combined output fasta

file_list = [] 
with open('output.fasta', 'w+') as w_file:
    for filen in file_list:
        with open(filen, 'rU') as o_file:
            seq_records = SeqIO.parse(o_file, 'fasta')
            SeqIO.write(seq_records, w_file, 'fasta')
            
