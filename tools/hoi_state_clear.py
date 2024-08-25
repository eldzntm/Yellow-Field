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
            p_first = text.find('{',provinces_text)
            p_last = text.find('}',provinces_text)

            province = text[p_first:p_last]
            num_province = (re.sub(r'[^0-9]', ' ', province)).strip()
            
            manpower_text = text.find('manpower')
            m_first = text.find('=',manpower_text)
            m_last = text.find('\n',manpower_text)
            manpower = text[m_first+1:m_last].strip()
            
            state_category_text = text.find('state_category')
            s_first = text.find('=',state_category_text)
            s_last = text.find('\n',state_category_text)
            state_category = text[s_first+1:s_last].strip()
            
            resources_text = text.find('resources')
            if resources_text != -1:
                r_first = text.find('{',resources_text)
                r_last = text.find('}',resources_text)
                resources = text[r_first+1:r_last].strip()

        with open(file_path,'w') as f:
            f.write("""
state = {
	id = %s
	name = "STATE_%s"
    resources={
        %s
    }

	history={
		owner = LUX
		add_core_of = LUX
	}

	provinces = {
		%s
	}
    manpower = %s
    buildings_max_level_factor=1.000
	state_category=%s
	local_supplies=0.000
}
            """ % (numbers, numbers, resources if resources_text != -1 else "", num_province, manpower, state_category))
        