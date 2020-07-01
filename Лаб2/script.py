
import xml.etree.ElementTree as xml
tree = xml.parse('bd.xml')
root = tree.getroot()
print (root)

for child in root.findall('Team'):
    type = (child.get('type'))
    if type != "Men" :
        name = child.get('name')
        type = child.get('type')
        Results = child.find('Results')
        Win = int(Results.find('Win').text)
        if Win > 3 :
            print (name, "-", type, ";", "Количество побед:", Win)
