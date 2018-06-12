# Works with Python 3
# if you are using python 2.7 , remove the argument newline='' while opening the csv file

import os, glob, csv, argparse
import xml.etree.ElementTree as ET

def xml_to_csv(path, outputname):
  output_path = os.path.join(path,'{}_csv_data'.format(outputname))
  if not os.path.exists(output_path):
    os.mkdir(output_path)
  with open(os.path.join(output_path, '{}_data.csv'.format(outputname)), 'w', newline='') as csvfile:
    fieldnames = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    try:
      for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        filename = root.find('filename').text
        if not filename.endswith('.jpg'):
          filename +=  '.jpg'
        width = int(root.find('size').find('width').text)
        height = int(root.find('size').find('height').text)
        
        for object in root.findall('object'):
          bndbox = object.find('bndbox')
          xmin = int(bndbox.find('xmin').text)
          ymin = int(bndbox.find('ymin').text)
          xmax = int(bndbox.find('xmax').text)
          ymax = int(bndbox.find('ymax').text)
          name = object.find('name').text
          writer.writerow({'filename':filename, 'width': width, 'height': height, 'class': name, 'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax})
    except Exception as e:
      print ('Exception {}'.format(e))

def checkpath(path, outputname):
  if os.path.exists(path):
    xml_to_csv(path, outputname)
  else:
    print("Path doesn't exists")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--traindir", help='''Fullpath for Annoation xml files in your Training Directory''')
    parser.add_argument("--testdir", help='''Fullpath for Annoation xml files in your Testing Directory''')
    args = parser.parse_args()
    
    if args.traindir is None:
      print("No Training Directory Entered, skipping")
    else:
      checkpath(args.traindir, 'training')
      
    if args.testdir is None:
      print("No Testing Directory Entered, skipping")
    else:
      checkpath(args.testdir, 'testing')  
    
