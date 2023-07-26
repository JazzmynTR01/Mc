from pathlib import Path

# import final results as module in main.py
from overheads import summary_overheads as oh_result
from coh import result as coh_result
<<<<<<< HEAD
from profit_loss import result as pl_result
=======
from profit_loss import pl
from profit_loss import result as p1_result
>>>>>>> 05c0e97cc4ef18624c2ef97fbb2bf6026d4ff68d

fp_write = Path.cwd()/"summary_report.txt"
# create the text file
fp_write.touch()

# open the txt file 
with fp_write.open(mode="w", encoding="UTF-8" ) as file:
    # write summary in summary_report.txt file
    file.write(f'{oh_result}\n') 
    file.write(coh_result)
    file.write(p1_result)

    
# hello world