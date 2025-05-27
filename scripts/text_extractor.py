import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description="A script that extracts target tags and attribute pairs from a XML tree.")

parser.add_argument('--filter', type=str, help='target XML tag name')
parser.add_argument('--filepath', type=str, help='target file path')
parser.add_argument('--text', type=str, help='XML tag name for text')
parser.add_argument('--text_attr', type=str, help='XML tag attribute name for text data')
parser.add_argument('--audio', type=str, help='XML tag name for audio')
parser.add_argument('--audio_attr', type=str, help='XML tag attribute name for audio data')
args = parser.parse_args()

def traverse(node, node_list):
    node_list.append(node)  
    for child in node:
        traverse(child, node_list)

# 0. Parse
tree = ET.parse(args.filepath)
root = tree.getroot()
all_nodes = []
data = []

# 1. Traverse and filter
traverse(root, all_nodes)
tags = filter(lambda x: x.tag == args.filter, all_nodes)

# 2. Extract audio/text pair
for tag in tags:
    audio_tag = tag.find(args.audio)
    text_tag = tag.find(args.text)
    if not audio_tag is None and not text_tag is None and audio_tag.get(args.audio_attr) != "" and text_tag.get(args.text_attr) != "":
        data.append((audio_tag.get(args.audio_attr), text_tag.get(args.text_attr)))

# 3. Post processing
# Define a necessary function
def transform(datum):
    audio, text = datum
    pass

data_proc = map(lambda x:transform(x), data)

# 4. Write
with open('dataset.txt','w') as f:
    for audio, text in data_proc:
        f.write("{}|{}|{}\n".format(audio,0,text))
