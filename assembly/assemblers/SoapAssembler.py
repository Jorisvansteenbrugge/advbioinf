#!/usr/bin/env python

from sys import argv
import subprocess as sp
import os

class SoapAssembler(object):
    
    def __init__(self, workdir):
        print(__name__)
        self.workdir = workdir
        self.contigFile = self.workdir + "/soapGraph.contig"


    def assemble(self, readType, readFiles, ksize):
        self.readFiles = readFiles
        soapconfig = self.soapConfig()
        soap = "soapdenovo-63mer all -s {} -K {} -R -o {}".format(soapconfig,
                                                                  ksize,
                                                                  "soapGraph")
        os.chdir(self.workdir)
        sp.call(soap, shell = True)

        
        
    def soapConfig(self):
        scriptPath = os.path.dirname(os.path.realpath(argv[0]))
        soap_template = scriptPath + "/soapConfig"
        soap_config = self.workdir + "/soapConfig"

        with open(soap_template) as inFile, open(soap_config,"w") as outFile:
            for line in inFile:
                outFile.write(line)
            outFile.write("q1={}\n".format(self.readFiles[0]))
            outFile.write("q2={}".format(self.readFiles[1]))
        return soap_config

    def getContigFile(self):
        return self.contigFile
