import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
 
def read_from_db (username, password, connectString, mode=None, save=True):
 
    connection = cx_Oracle.connect(username, password, connectString)
    with connection:
        try:
            df = pd.read_sql_query("SELECT\
                                      wc.wait_class                    AS waitclass,\
                                      TRUNC(begin_time, 'MI')          AS sample_time,\
                                      round((wh.time_waited) / wh.intsize_csec, 3) AS DB_time\
                                    FROM V$SYSTEM_WAIT_CLASS wc,\
                                      v$waitclassmetric_history wh\
                                    WHERE wc.wait_class != 'Idle'\
                                          AND wc.wait_class_id = wh.wait_class_id\
                                    UNION\
                                    SELECT\
                                      'CPU'                   AS waitclass,\
                                      TRUNC(begin_time, 'MI') AS sample_time,\
                                      round(VALUE/100, 3)         AS DB_time\
                                    FROM v$sysmetric_history\
                                    WHERE GROUP_ID = 2\
                                          AND metric_name = 'CPU Usage Per Sec'\
                                    ORDER by sample_time, waitclass",
                                   connection)
            if save:
                df.to_csv('results.csv')
            return df
        except cx_Oracle.DatabaseError as dberror:
            print dberror
 
def read_from_file(filename):
    return pd.read_csv(filename, parse_dates=['SAMPLE_TIME'])
 
 
if __name__ == '__main__':
    style.use('ggplot')

    # Add credentials here
    df = read_from_db(username='', password='', connectString='', mode=cx_Oracle.SYSDBA, save=True)
    # df = read_from_file('results.csv')
     
    pdf = df[df['WAITCLASS'] == 'CPU']

    pdf.plot(x='SAMPLE_TIME', y='DB_TIME')
    plt.show()
