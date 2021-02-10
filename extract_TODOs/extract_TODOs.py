import os
import sys
import pandas as pd

def explore_directory(directory):
    for root, sub_directory, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            yield path, file


def extract_TODOs(directory, extract_following_lines=False, ignore_directories = ['dist']):
    df = pd.DataFrame(columns=["Description", "File", "Full Path", "Line", "Priority"])
    directory_location = os.path.dirname(directory)

    for path, file in explore_directory(directory):
        # Add '/' to make sure that it's a directory with that specific name
        ignore_directories = ['/' + ignore_directory + '/' for ignore_directory in ignore_directories]
        if any(ignore_directory in path for ignore_directory in ignore_directories):
            continue

        with open(path, 'r') as f:
            file_content = None
            try:
                file_content = f.read()
                # print("Reading: ", file)
            except:
                print(file, " ignored.")
                continue
            lines = file_content.splitlines(False)
            for i in range(len(lines)):
                if "TODO" in lines[i]:
                    content = lines[i]
                    
                    if extract_following_lines:
                        # Check type of comment
                        char = None
                        if "//" in content:
                            char = "//"
                        elif "#" in content:
                            char = "#"

                        # Get attached comments
                        j = i+1
                        while j<len(lines):
                            if char in lines[j] and "TODO" in lines[j]:
                                break
                            content += ' ' + lines[j]
                            j += 1

                    df.loc[len(df)] = [content, file, os.path.relpath(path, directory_location), i+1, ""]
            
        
    return df
    

if __name__ == "__main__":
    '''
    Usage example:
        python extract_TODOS.py directory_to_explore save_path.csv
    '''
    directory, save_path = sys.argv[1:]

    df = extract_TODOs(directory)
    df.to_csv(save_path, index=False)
