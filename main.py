import json
from tokusei import TokuseiManager

tokuseis = TokuseiManager()

tokuseis.generateTokuseiXmlSchema('tokuseis.xml.schema')

with open('tokuseiFiles.json', 'w') as outputfile:
  json.dump(tokuseis.getTokuseiMap(), outputfile, indent=2)