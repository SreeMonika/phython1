"""
import json

with open("test_json.json","r") as fp:
    #data=fp.read()
    #print(data)
    #Note: json.loads will convert str into dict
    #json_dict=json.loads(data)

    # json.load directly returns data from file into dictionary
    json_dict=json.load(fp)
    print(json_dict)
    print(json_dict["myinfo"]["firstname"])
    json_dict["myinfo"]["firstname"]="Rishi"
    json_dict["myinfo"]["lastname"] = "Goswami"
    json_dict["myinfo"]["Age"] = 24
    print(json_dict["myinfo"]["technologies"]["skills"])
    json_dict["myinfo"]["technologies"]["skills"][0]="Ansible"
    json_dict["myinfo"]["technologies"]["skills"][1]="Dockers"
    json_dict["myinfo"]["technologies"]["skills"][2]="Kubernetes"
    print(json_dict)
    #for skill in json_dict["myinfo"]["technologies"]["skills"]:
        #skill

with open("newtest_json.json","w") as ft:
    json.dump(json_dict,ft,indent=4)
    string_object=json.dumps(json_dict,indent=4)
    print(string_object)
"""
"""
import xmltodict
#print(dir(xmltodict))

with open("newtest_xml.xml","r") as fp:
    xml_data=fp.read()
    # Note: parse method converts str object into dict
    xml_dict=xmltodict.parse(xml_data)
    print(xml_dict["myinfo"]["firstname"])
    xml_dict["myinfo"]["firstname"]="ashutosh"
    xml_dict["myinfo"]["lastname"]="kumar"
    print(xml_dict)
    print(xmltodict.unparse(xml_dict,pretty=True))

with open("duplicatexml.xml","w") as fp:
    fp.write(xmltodict.unparse(xml_dict,pretty=True))
"""

import yaml

with open("test_yaml.yml","r") as fp:
    #print(fp.read())
    yaml_data=yaml.load(fp,Loader=yaml.FullLoader)
    yaml_data["myinfo"]["firstname"]="satya"
    print(yaml_data)

with open("duplicate_yaml.yml","w") as fp:
    fp.write(yaml.dump(yaml_data))