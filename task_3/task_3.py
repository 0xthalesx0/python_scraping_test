import math
import os
from datetime import datetime, timezone
import pandas as pd

file_names = []
file_extensions = []
file_paths = []
file_sizes = []
file_modified = []


def task_3(dir, isrecursive):
    with os.scandir(dir) as it:
        for entry in it:
            if not entry.is_file():
                task_3(f"{dir}\\{entry.name}", True)

            if not entry.name.startswith('.') and entry.is_file():
                index = entry.name.rfind('.')

                file_names.append(entry.name[:index])
                file_extensions.append(entry.name[index:].lower())

                path = f"{dir}\\{entry.name}"
                file_paths.append(path)
                stats = os.stat(path)

                file_sizes.append(convert_size(stats))

                modified = datetime.fromtimestamp(stats.st_mtime)
                file_modified.append(modified)

    if not isrecursive:
        return create_dataframe()


def create_dataframe():
    dataframe = pd.DataFrame(
        {
            'Name': file_names,
            'Extensions': file_extensions,
            'Path': file_paths,
            'Size (KB)': file_sizes,
            'Last Modified': file_modified
        }
    )
    return dataframe


def convert_size(stats):
    return int(math.ceil(stats.st_size / float(1 << 10)))


df = task_3(input("Type your directory: "), False)

excel_name = input("Type the final file name: ")
df.to_excel(f'{excel_name}.xlsx')

print("Completed.")
