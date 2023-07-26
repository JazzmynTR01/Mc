from pathlib import Path
from overheads import summary_overheads
from coh import hand
from coh import result as coh_result
from profit_loss import pl
from profit_loss import result as p1_result

fp_write = Path.cwd()/"summary_report.txt"
fp_write.touch()



with fp_write.open(mode="w", encoding="UTF-8" ) as file:
    file.write(f'{summary_overheads}\n') 
    file.write(coh_result)
    file.write(p1_result)

    
# hello world