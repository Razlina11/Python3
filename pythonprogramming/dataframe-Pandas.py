import pandas as pd
data={"Name":["Razlina","Subash","Sharmi"],"CGPA":[9.2,9.2,9.2]}
s=pd.DataFrame(data)
s.index+=1
print(s)
