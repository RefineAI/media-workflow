from pliers.extractors import GoogleVisionAPIFaceExtractor

ext = GoogleVisionAPIFaceExtractor()

result = ext.transform('/home/icarus/projects/pliers/pliers/tests/data/image/obama.jpg').to_df()

print result