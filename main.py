import sqlite3
from bs4 import BeautifulSoup

con = sqlite3.connect("diary.db")
cur = con.cursor()
res = cur.execute("SELECT Z_PK, ZNOTE, date(ZCREATEDATE / 1000, 'unixepoch') FROM ZDIARY").fetchall()

previous_id = next_id = None
l = len(res)

for index, row in enumerate(res):
    if index > 0:
        previous_id = res[index - 1][0]
    if index < (l - 1):
        next_id = res[index + 1][0]

    current_id = row[0]
    note_html = row[1]
    created_at = row[2]

    with open('layout.html', 'r') as layout_file:
        layout_soup = BeautifulSoup(layout_file, 'html.parser')
        soup = BeautifulSoup(note_html, 'html.parser')

        for img in soup.find_all('img'):
            img_url = img['src']

            if img['type'] == 'emoticon':
                img.decompose()
                continue

            img_url = "." + img_url[4:]
            img['src'] = img_url

        card_text = layout_soup.find("div", {"class": "card-text"})
        card_text.insert(1, soup)

        previous_btn = layout_soup.find("a", {"id": "previous_btn"})
        previous_btn['href'] = str(previous_id) + ".html" if previous_id != None else "#"
        
        next_btn = layout_soup.find("a", {"id": "next_btn"})
        next_btn['href'] = str(next_id) + ".html" if next_id != None else "#"

        card_header = layout_soup.find("div", {"class": "card-header"})
        card_header.insert(1, str(created_at))

        with open(f'./content/{current_id}.html', 'w') as f:
            f.write(layout_soup.prettify())
            f.close()