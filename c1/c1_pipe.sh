sizeseq -sequences $1 -descending y -outseq $(basename $1 .fasta)_sorted.fasta
nthseq -sequence $(basename $1 .fasta)_sorted.fasta -number 1 -outseq $(basename $1 .fasta)_first.fasta
pepstats -sequence $(basename $1 .fasta)_first.fasta -outfile $(basename $1 .fasta)_stats
cat $(basename $1 .fasta)_stats | grep "Residues = " | cut -d " " -f 7

#as oneliner:
# sizeseq -sequences plants.fasta -descending y -outseq stdout |nthseq -sequence stdin -number 1 -outseq stdout | pepstats -sequence stdin -outfile stdout | grep "Residues = " | cut -d " " -f 7
