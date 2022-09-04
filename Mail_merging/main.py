from data_manager import DataManager


FILE_NAME_NAME = './input/names.json'
FILE_NAME_TEMPLATE = './input/template.txt'

name_adjuster = DataManager(FILE_NAME_TEMPLATE,FILE_NAME_NAME)
name_adjuster.write_data_to_output()