import sys
import os
import logging
from traverse_directory import Traverse_directory

def main():
    path_directory = sys.argv[1] #argv[0] is main.py

    logging.basicConfig(filename='logs.log', level=logging.INFO)

    if not os.path.isdir(path_directory):
        logging.error(f'Path {path_directory} is not directory')   
        return
    
    td = Traverse_directory()
    td.run(path_directory) 

    #Выполняем логирование
    for s in td.results:
        if s.is_directory == True:
            logging.info(f"DIRECTORY: name: '{s.name}', parent_directory: '{s.parent_directory}'")
        else:
            logging.info(f"FILE: name: '{s.name}', extension: '{s.ext}', parent_directory: '{s.parent_directory}'")           

main()

