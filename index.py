import sqlite3
from bs4 import BeautifulSoup
import os
import logging

journie_path = "./Journie"

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

con = sqlite3.connect("diary.db")
cur = con.cursor()

if not os.path.exists(journie_path):
    os.makedirs(journie_path)
    logging.info(f"Created directory '{journie_path}'")

logging.info("Started")

with open('indice.html', 'r') as f:
    index_soup = BeautifulSoup(f, 'html.parser')    
    for row in cur.execute("SELECT Z_PK, strftime('%d-%m-%Y', datetime(ZCREATEDATE + 978307200, 'unixepoch')) FROM ZDIARY"):
        id = row[0]
        date = row[1]

        tr_html = f"""<tr>
            <th scope="row"><a href="diary/{row[0]}.html">{id}</a></th>
            <td>{date}</td>
        </tr>
        """

        new_tr = BeautifulSoup(tr_html, 'html.parser')

        index_soup.html.body.div.table.tbody.append(new_tr)

        with open(f'{journie_path}/table.html', 'w') as table_file:
            table_file.write(index_soup.prettify())
            table_file.close()

logging.info("Done")