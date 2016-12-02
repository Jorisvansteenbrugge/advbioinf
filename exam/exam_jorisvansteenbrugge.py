#!/usr/bin/env python
"""
Program that predicts transcripts base on a fasta sequence using Augustus
and compares the predicted transcripts to a reference annotation set.
"""
from __future__ import division

__author__ = "Joris van Steenbrugge (950416798110)" 
__date__ = "25/11/2016"
__email__ = "joris.vansteenbrugge@wur.nl" 

from sys import exit
from os import path
import subprocess as sp
import argparse

class Transcript(object):
    """Class to store Transcript objects
    """
    def __init__(self, start, stop, ID, parent):
        """Constructor to create local variables from given parameters
        """
        self.start = start
        self.stop = stop
        self.ID = ID
        self.parent = parent

    def __str__(self):
        """Overriden string method to print the transcript in tsv format
        """
        return "{}\t{}\t{}\t{}\n".format(self.start, self.stop,
                                    self.augID, self.geneID)
    

def runAugustus(query, output, species="saccharomyces_cerevisiae_S288C",
                 gene_model="complete"):
    """Runs Augustus on the command line using subprocess.
    
        Keyword arguments:
            query -- FileName in fasta format to be annotated by
                     Agustus.

            species -- Trained species dataset by augustus to use
                       in the annotation of the query.

            output -- FileName for the output gff file.

            gene_model -- Tells Augustus to annotate
                          e.g. only complete genes.

        If the output file already exists, the subprocess call  
        is silently ignored.
    """
    cmd = "augustus --genemodel={} --species={} --gff3=on {} > {}".format(
                                                                    gene_model,
                                                                    species, 
                                                                    query, 
                                                                    output) 
    if path.exists(output):
        return
    else:
        try:
            sp.check_call(cmd, shell=True)
        except sp.CalledProcessError:
            print("Augustus failed to run")
            exit(1)
        

def parseGFF(file_name, transcript_name):
    """Parses a GFF file and returns a list of transcript objects
    
        Keyword arguments:
            file_name -- The fileName of the gff file.
        
            transcript_name -- The name of a transcript in the gff file
                                (e.g mRNA/transcript etc.).

        Returns:
            transcript_list -- A list object containing Transcript objects

        The transcript_name variable is used to determine what records in
        the GFF file are stored as a Transcript object.
    """
    transcript_list = []
    with open(file_name) as in_file:
        for line in in_file:
            if not line.startswith("#"): #if not a comment line
                line = line.strip().split()
                if line[2] == transcript_name: #Determine if the record is a transcript
                    attributes = line[8].split(";")
                    #filter out ID and parent form the attributes column
                    # using list comprehension
                    ID = "".join([x.split("=")[1] for x in attributes if "ID" in x])
                    parent = "".join([x.split("=")[1] for x in attributes if "Parent" in x])
                    
                    #Append the gff record to the transcript_list
                    trans = Transcript(line[3], line[4],ID, parent)
                    transcript_list.append(trans)
           
    return transcript_list



def calcTPFN(predict, ref):
    """Calculates the tp, fn an returns those with tp_transcript objects

        Keyword arguments:
            predict -- A list containing predicted Transcript objects 
                      (from Augustus).
        
            ref -- A list containing reference Transcript objects
                  (from the reference annotation).

        Returns:
            tp -- The number of true positives found as integer.
        
            fn -- The number of false negatives found as integer.
    
            tp_transcripts -- A list of true positive Transcript objects
                              Containing start, end, augustusID and geneID.

        A transcript is a true positive when a transcript is present in both the reference
        and predicted transcripts

        A transcript is a false negative when a transcript is present in the reference
        but is not in the list of predicted transcript.

        A transcript is "present" if the start and end positions are identical
        in both the reference and predicted transcript annotations.
    """
    tp = 0
    fn = 0
    tp_transcripts = []
    for ref_transcript in ref:
        found = False
        #Compare eash ref transcript with all predicted transcripts
        for predict_transcript in predict: 
            #Determine if te ref is identical to the predicted transcript
            if (ref_transcript.start == predict_transcript.start and
                    ref_transcript.stop == predict_transcript.stop):
                
                #If we have a true positive, create a tp transcript Object
                # and append it to the tp_transcripts list
                trans = Transcript(ref_transcript.start, ref_transcript.stop,
                                    None, None)
                trans.augID = predict_transcript.ID
                trans.geneID= ref_transcript.ID
                tp_transcripts.append(trans)
                tp += 1
                found = True
                break
        #if no match/tp was found we have a true negative
        if not found:
            fn +=1

    return tp, fn, tp_transcripts

def calcFP(predict, ref):
    """Returns the number of false positives

        Keyword arguments:
            predict -- A list containing predicted Transcript objects
                      (from Augustus).
        
            ref -- A list containing reference Transcript objects
                  (from the reference annotation).
        Returns:
            fp -- The number of false positives found as integer

        A transcript is a false positive if the transcript is predicted
        but not present in the reference annotation.

        A transcript is "present" if the start and end positions are identical
        in both the reference and predicted transcript annotations.
    """
    fp = 0
    for predict_transcript in predict:
        found = False
        #compare each predicted transcript to all reference transcripts
        for ref_transcript in ref:
            #Determine if the predicted is identical to the ref transcript
            if (predict_transcript.start == ref_transcript.start and
                    predict_transcript.stop == ref_transcript.stop):  
                found = True
                break

        #if no match/tp was found we have a false positive
        if not found:
            fp += 1
    return fp

def reportOutput(tp_transcripts, output):
    """Writes the tp transcripts to the output file tsv formatted

        Keyword arguments:
            tp_transcripts -- A list with Transcript objects.

            output -- The fileName of the output tsv file.
    """
    with open(output, "w") as out_file:
        for trans in tp_transcripts:
            out_file.write(str(trans))

def parseArguments():
    """Parses the command line arguments using argparse

        Returns:
            -- An argument object that contains the declared
               command line arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-ref", dest="refGFF", required = True, 
        help = "The reference annotation in GFF format")
    parser.add_argument("-seq", dest="fasta", required = True,
        help = "The sequence in fasta format to be annotated")
    parser.add_argument("-o", dest="output", required = False,
        default = "output.tsv", help = "The tab-seperated output file " +
                                       "containing the true positive transcripts")

    return parser.parse_args()
    

if __name__ == "__main__":
    #Defining the fileName variables
    args = parseArguments()
    seq = args.fasta
    anno = args.refGFF
    output = args.output
    augustus_out = "augustus.gff"


    #Run Augustus and parse gff files    
    runAugustus(seq, augustus_out)
    anno_trans = parseGFF(anno, "mRNA") #anno
    augustus_trans = parseGFF(augustus_out, "transcript")

    #Doing calculations to determine true positives, false negatives
    # and false positives. Based on these numbers the recall and precision
    # rate is calculated
    tp, fn, tp_transcripts = calcTPFN(augustus_trans, anno_trans)
    fp = calcFP(augustus_trans, anno_trans)
    try:
        recall = (tp/(tp+fn))
        precision = (tp/(tp+fp))
        
        #Print the recall and precision to the console
        print("Recall: {:.2f}".format(recall))
        print("Precision: {:.2f}".format(precision))
    except ZeroDivisionError:
        print("One of the gff files might be empty.." +
            "Please check: {} and {}".format(augustus_out,
                                            anno))
        exit(1)



    #Write true positive transcripts to the output file
    reportOutput(tp_transcripts, output)
