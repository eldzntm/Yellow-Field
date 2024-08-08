import os
import re

dir_path = "history\states"

for (root, directories, files) in os.walk(dir_path):

    for file in files:
        file_path = os.path.join(root, file)
        numbers = re.sub(r'[^0-9]', '', file_path)
        numbers = numbers[0:3]
        with open(file_path,'r') as f:
            text = f.read()
            id_text = text.find('id')
            name = text.find('name')
            
            numbers = (re.sub(r'[^0-9]', ' ', text[id_text:name])).strip() 

            provinces_text = text.find('provinces')
            first = text.find('{',provinces_text)
            last = text.find('}',provinces_text)

            province = text[first:last]
            num_province = (re.sub(r'[^0-9]', ' ', province)).strip()

        with open(file_path,'w') as f:
            f.write("""
state = {
	id = %s
	name = "STATE_%s"

	history={
		owner = ZZZ
		add_core_of = ZZZ
	}

	provinces = {
		%s
	}
    manpower = 1
    buildings_max_level_factor=1.000
	state_category=wasteland
	local_supplies=0.000
}
            """ % (numbers, numbers, num_province))
        