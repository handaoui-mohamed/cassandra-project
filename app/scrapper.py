import requests
from bs4 import BeautifulSoup
from app.models.match import Match, results

PARSER = "html.parser"
BASE_URL = "https://eu-football.info/_matches.php?page="
PAGES = 540


def scrap():
    for page_index in range(1, 2):
        url = BASE_URL + str(page_index)
        print("Fetching url = " + url)
        result = requests.get(url)
        if(result.status_code == 200):
            page = result.content
            soup = BeautifulSoup(page, PARSER)

            table = soup.find("table", "t2 b3")
            # print(table.prettify())
            # table_body = table.find("tbody")
            table_rows = table.find_all("tr")

            for row in table_rows[1:-1]:
                cells = row.find_all("td")
                match_id = cells[0].get_text().strip().replace('.', '')

                match_date = cells[1].get_text().strip().split('.')
                match_date[0], match_date[2] = match_date[2], match_date[0]
                match_date = '-'.join(str(x) for x in match_date)

                match_venue = cells[2].get_text().strip()
                tournament = cells[3].get_text().strip()
                # embed score and competitor name

                score = cells[5].get_text().strip().split(":")
                score[0] = int(score[0])
                score[1] = int(score[1])

                competitor_1 = {}
                competitor_1[cells[4].get_text().strip()] = score[0]

                competitor_2 = {}
                competitor_2[cells[6].get_text().strip()] = score[1]

                result = results.DRAW  # draw
                if(score[0] > score[1]):
                    result = results.WIN  # competitor 1 is the winner
                elif(score[0] < score[1]):
                    result = results.LOSS  # competitor 2 is the winner

                match = Match.create(
                    date=match_date,
                    venue=match_venue,
                    tournament=tournament,
                    competitor_1=competitor_1,
                    competitor_2=competitor_2,
                    result=result
                )

                match.save()

                # print(match.get_data())
