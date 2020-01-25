from xml.dom import minidom

doc_xml = minidom.Document()
root = doc_xml.createElement('root')
doc_xml.appendChild(root)

leaf = doc_xml.createElement('leaf')
text = doc_xml.createTextNode('Text element with attributes')
leaf.appendChild(text)
leaf.setAttribute('color', 'white')
root.appendChild(leaf)

leaf_cdata = doc_xml.createElement('leaf_cdata')
cdata = doc_xml.createCDATASection('<em>CData</em> can contain <strong>HTML tags</strong> without encoding')
leaf_cdata.appendChild(cdata)
root.appendChild(leaf_cdata)

branch = doc_xml.createElement('branch')
branch.appendChild(leaf.cloneNode(True))
root.appendChild(branch)

mixed = doc_xml.createElement('mixed')
mixed_leaf = leaf.cloneNode(True)
mixed_leaf.setAttribute('color', 'black')
mixed_leaf.setAttribute('state', 'modified')
mixed.appendChild(mixed_leaf)
mixed_text = doc_xml.createTextNode('Do not use mixed elements if it possible.')
mixed.appendChild(mixed_text)
root.appendChild(mixed)

xml_str = doc_xml.toprettyxml(indent="  ")
with open("minidom_example.xml", "w") as f:
    f.write(xml_str)
