'''
Fix the regular expression used in the rearrange_name function so that it can match middle names, 
middle initials, as well as double surnames.
'''

import re
def rearrange_name(name):
  result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)



'''
Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, 
after the process id.
'''

import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: [A-Z]+"
    result = re.search(regex, log_line)
    if result is None:
        return None
    word_idx = result[0].find(" ") + 1
    return f"{result[1]} ({result[0][word_idx:]})"

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)