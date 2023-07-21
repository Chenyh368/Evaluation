import argparse
import xml.etree.ElementTree as ET

def read_Pascal_VOC(xml_file,do_0_based):
    # Pascal VOC is 1-based, but more recent formats like MS COCO are 0-based
    # see, e.g., https://github.com/Ricardozzf/maskrcnn-benchmark/commit/da8f99927eb945d3e66985d5e070fb55db472de6
    if do_0_based:
        to_subtract = 1
    else:
        to_subtract = 0
    tree = ET.parse(xml_file)
    root = tree.getroot()
    boxes = dict()
    for box in root.iter('object'):
        name = box.find('name').text
        bb = box.find('bndbox')
        # dict to remove any ambiguity ordering-wise
        coords = dict(xmin = bb.find('xmin').text,
                      ymin = bb.find('ymin').text,
                      xmax = bb.find('xmax').text,
                      ymax = bb.find('ymax').text)
        coords = {k:int(v)-to_subtract for k,v in coords.items()}
        if name in boxes:
            boxes[name] = boxes[name] + [coords]
        else:
            boxes[name] = [coords]
    return boxes

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir',
                    default='./',
                    help='folder containing all images')
args = parser.parse_args()

