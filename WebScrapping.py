from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mysql.connector

#db = mysql.connector.connect(host="localhost", port="3306", user="root", password="Rikelme10@", database="results")
#mycursor = db.cursor()
#mycursor.execute("CREATE TABLE livescore(time VARCHAR(50))") > nessa linha foi criado a tabela LIVESCORE, com o atributo TIMES




#from urllib.parse import urljoin


driver = webdriver.Chrome(executable_path=f'./chromedriver.exe')
driver.get('https://www.livescores.com/')
time.sleep(7)
#Abaixo o código tira os cookies ao entrar no site
tab_cookies = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/button")
tab_cookies.click()
time.sleep(7)
#abaixo o código entra na table ao vivo do site, o primeiro passo para capturar os jogos e estatisticas acontecendo
tab_aovivo = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/a")
tab_aovivo.click()

#abaixo o código captura  xpath das janelas ao vivo do esporte
div_main = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]")
#manusear o conteudo do div_mae, transformar em html
html_content = div_main.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())
#Estudando o código transformado em HTML cheguei nas conclusões abaixo, onde só o id é dinamico de cada jogo
#<span class="Nh" id="0-697686__match-row__home-team-name"> - Id do jogo e a classe nome do time mandante
#<span class="Qh" id="0-697686__match-row__home-team-score"> - Id do jogo e placar do time mandante
#<span class="Rh" id="0-697686__match-row__away-team-score"> Id do jogo e placar do time visitante
#<span class="Nh" id="0-697686__match-row__away-team-name"> Id do jogo e a classe nome do time visitante
#<span class="ug qg tg" id="0-697686__match-row__status-or-time"> Tempo de jogo

home = soup.find_all(class_='Lh')
away = soup.find_all(class_='Mh')
home_score = soup.find_all(class_ = 'Qh')
away_score = soup.find_all(class_ = 'Rh')
time_game = soup.find_all(class_ = 'ug qg tg')
placar_jogo = []
#print(testando)
#league_name = soup.find_all(class_ = 'hb')
#el = soup.find_all("div", class_="Jc Nc Mc", href=True)
#print(el['href'])

#Pegando os links SOMENTE das partidas ao vivo - para isso usar a classe > Jc Nc Mc
for i, element in enumerate(home):
   try:
#  print(league_name[i].text)
   #print(time_game[i].text + ' ' + home[i].text + ' ' + home_score[i].text + ' vs ' + ' ' + away_score[i].text + ' ' + away[i].text)
      x = (time_game[i].text + ' ' + home[i].text + ' ' + home_score[i].text + ' vs ' + ' ' + away_score[i].text + ' ' + away[i].text)
   #  print(home[i].text + ' ' + home_score[i].text + ' vs ' + ' ' + away_score[i].text + ' ' + away[i].text)
      placar_jogo.append(x)
      print(placar_jogo)
   except:
      pass
   #comando_sql = "INSERT INTO time, VALUES(%s)"
   #valores = (placar_jogo)
   #mycursor.execute(comando_sql,valores)
   #db.commit()
#stats_lista = []

for data in soup.find_all('div', class_='Jc Nc Mc'):
    for links in data.find_all('a'):
       try:
          link1 = (links.get('href')) #for getting link
          #        print(links.text) #for getting text between the link
          link2 = "https://www.livescores.com"
          link_matches = (link2+link1)
          driver.get(link_matches)
          tab_stats = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/a[3]")
          time.sleep(2)
          tab_stats.click()
          time.sleep(2)
          #tab_stats_chutes = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]")
          tab_stats_chutes = driver.find_element_by_xpath("/html/body/div[2]/div[2]")
          html_content_stats = tab_stats_chutes.get_attribute('outerHTML')
          soup2 = BeautifulSoup(html_content_stats, 'html.parser')
          print(soup2.prettify())


          nome_mandante = soup2.find_all(class_='Ge')
          nome_visitante = soup2.find_all(class_='He')
          score_mandante = soup2.find_all(id='match-detail__home__score')
          score_visitante = soup2.find_all(id='match-detail__away__score')
          Stats_name_home = soup2.find_all(class_='Of')
          Stats_home = soup2.find_all(class_='Jf')
          Stats_name_away = soup2.find_all(class_='Pf')
          Stats_away = soup2.find_all(class_='Kf')
          stats_lista = []
   # Pegando os links SOMENTE das partidas ao vivo - para isso usar a classe > Jc Nc Mc
          for j, element in enumerate(Stats_name_home):
                #  print(league_name[i].text)
                # print(time_game[i].text + ' ' + home[i].text + ' ' + home_score[i].text + ' vs ' + ' ' + away_score[i].text + ' ' + away[i].text)
                #print(home[i].text + ' ' + home_score[i].text + ' vs ' + ' ' + away_score[i].text + ' ' + away[i].text)
                #print(Stats_name_home[j].text + ':' + Stats_home[j].text + ':' + Stats_away[j].text)
                #resultados_livematches = (nome_mandante[j].text + " " + score_mandante[j].text + " " + "vs" + " " + score_visitante[j].text + " " + nome_visitante[j].text)
                #resultados_livematches = (nome_mandante[j].text + " " + "vs" + " " + nome_visitante[j].text)
                stats_times = (Stats_name_home[j].text + ' : ' + Stats_home[j].text + ' : ' + Stats_away[j].text)
                stats_lista.append(stats_times)
                #print(placar_jogo)
                #print(resultados_livematches)
                print(stats_lista)

       except:
             pass



