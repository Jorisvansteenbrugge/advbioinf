
class BaseMapper(object):
    toolIndex = {1: "bwa mem",
                 2: "bowtie2"
                }

    def __init__(self, tool_num, read_type, read_files, output):
        self.tool = self.toolIndex[tool_num]
        self.read_type = read_type 
        self.read_files = read_files
        self.output = output


    def map(self):
        self.mapper = None
        if self.tool = "bwa mem":
            
