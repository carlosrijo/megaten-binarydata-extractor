import json
from tokusei import TokuseiManager
from basic_features import BasicFeaturesManager

tokuseis = TokuseiManager()
print('Loading items\' tokusei (SI slot 3)...')
tokuseisMap = tokuseis.getTokuseiMap()
print('Generating tokusei\' XML schema...')
tokuseis.generateTokuseiXmlSchema('tokuseis.xml.schema')
print('Tokusei processing complete.')

with open('tokuseiFiles.json', 'w') as outputfile:
  json.dump(tokuseis.getTokuseiMap(), outputfile, indent=2)

basicFeatures = BasicFeaturesManager()
print('Loading items\' basic features...')
basicFeatures.getBasicFeaturesMap()
print('Generating basic features\' XML schema...')
basicFeatures.generateBasicFeatureXmlSchema('basicFeatures.xml.schema')
print('Basic features processing complete.')

with open('basicFeaturesFiles.json', 'w') as outputfile:
  json.dump(basicFeatures.getBasicFeaturesMap(), outputfile, indent=2)
