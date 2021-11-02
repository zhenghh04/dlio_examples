import vanidl
from vanidl.analyzer import VaniDL
profile = VaniDL()
#Load darshan file
status = profile.Load("./res.darshan")
#Get Job Summary
summary = profile.GetSummary()
tl = profile.CreateIOTimeline()
import matplotlib.pylab as plt
# Print High level summary 
profile.PrintSummary()

## I/O timeline 
plt.figure(figsize=(20,4))
plt.grid()
plt.plot(tl['time_step']/1000, tl['read_count'], label='read')
plt.plot(tl['time_step']/1000, tl['write_count'], label='write')
plt.xlabel("Time (second)")
plt.ylabel("# of IO operation")
plt.savefig("timeline.png")
#plt.show()

import pprint
pp = pprint.PrettyPrinter(indent=1)
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print("Size of dataset (bytes)")
pp.pprint(profile.GetFileSizes())
    
df = profile.GetDXTAsDF()
pp.pprint("Files used in the application")
pp.pprint(df['Filename'].unique().tolist())

for file in df['Filename'].unique():
    print("I/O performed on file {}: {:0.2f} MB".format(file,float(profile.GetIOSize(filepath=file))/1024.0/1024.0))

##  Generate Timeline
profile.CreateChromeTimeline(location="./", filename="timeline.json")
#tensorboard_dir="log_dir"
#val = profile.CreateMergedTimeline(tensorboard_dir, "./", "merge", save=True, split_by_ranks=True, timeshift=2.745017)
