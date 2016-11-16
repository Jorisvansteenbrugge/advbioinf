
import subprocess as sp

class BaseAnnotator(object):
    tool_index = {1: "trnascan"
                }

    def __init__(self, tool_num, in_file, out_file):
        self.tool = self.tool_index[tool_num]
        self.in_file = in_file
        self.out_file = out_file



    def annotate(self):
        cmd_list = []
        if self.tool == "trnascan":
            trnascan = "trnascan-1.4 {} -o {}".format(self.in_file, self.out_file)
            print(trnascan)
            cmd_list.append(trnascan)


        for command in cmd_list:
            sp.call(command, shell = True)

