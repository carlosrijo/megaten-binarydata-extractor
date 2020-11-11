import glob
import json
from xmlparser import XmlParser
from config import base_tokusei_server_files_directory

class TokuseiManager:

  def __init__(self):
    self.filePattern = '{serverBasePath}/tokusei_*.xml'.format(serverBasePath=base_tokusei_server_files_directory)
    self.filenamesList = glob.glob(self.filePattern)
    self.tokuseiMap = {}

  def generateTokuseiXmlSchema(self, outputFileName):
    XmlParser.printXmlSchemaFromXmlFileList(self.filenamesList, outputFileName)

  def getTokuseiMap(self, reloadMap = False, objForSingleElems = False):
    if not self.tokuseiMap: reloadMap = True
    if reloadMap: self.__loadTokuseiMap(objForSingleElems)
    return self.tokuseiMap

  def __loadTokuseiMap(self, objForSingleElems = False):
    objs = XmlParser.parseXmlObjectFromFiles(self.filenamesList, objForSingleElems)
    # Convert parsing to a more "tokusei" readable dictionary
    for obj in objs:
      newTokusei = {}
      for item in obj['Tokusei']:
        if isinstance(item, str):
          newTokusei[item] = obj['Tokusei'].get(item)
        else:
          for key in item:
            if key == 'element': print('an element')
            newTokusei[key] = item.get(key)
      self.tokuseiMap[newTokusei['ID']] = newTokusei

  