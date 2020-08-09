from utils import COMP_utils

class Extractor:

    def __init__(self, baseInputDirPath, baseOutputDirPath):
        self.baseInputDirPath = baseInputDirPath
        self.baseOutputDirPath = baseOutputDirPath

    def extract(self, format, filename, option="load"):
        if ".sbin" in filename:
            COMP_utils.decryptSBIN(filename, self.baseInputDirPath, self.baseOutputDirPath)
        if ".bin" in filename:
            COMP_utils.bdPatch(filename, format, self.baseInputDirPath, self.baseOutputDirPath, option)
        else:
            COMP_utils.bdPatch(filename.replace("sbin", "bin"), format, self.baseOutputDirPath, self.baseOutputDirPath, option)
        return True

