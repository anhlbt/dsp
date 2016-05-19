from datetime import datetime as dt

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_str = '%m-%d-%Y'
(dt.strptime(date_stop, date_str) - dt.strptime(date_start, date_str)).days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_str = '%m%d%Y'
(dt.strptime(date_stop, date_str) - dt.strptime(date_start, date_str)).days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_str = '%d-%b-%Y'
(dt.strptime(date_stop, date_str) - dt.strptime(date_start, date_str)).days