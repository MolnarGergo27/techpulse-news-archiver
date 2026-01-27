import requests
import pandas as pd
import schedule
import time
import os
from datetime import datetime
from bs4 import BeautifulSoup

def get_tech_news():
    url = "https://news.ycombinator.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}    
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select(".titleline > a")        

        news_data = []
        for article in articles[:10]:  # Csak az első 10 hírt kérjük
            news_data.append({
                "Datum": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Cim": article.get_text(),
                "Link": article['href']
            })
            
        return news_data
    except Exception as e:
        print(f"Hiba történt a hírek lekérése során: {e}")
        return []

def save_to_excel(new_news):
    file_name = "tech_hirek_archivum.xlsx"
    df_new = pd.DataFrame(new_news)
    
    if os.path.exists(file_name):
        try:
            df_old = pd.read_excel(file_name)
            df_final = pd.concat([df_old, df_new], ignore_index=True)
            df_final = df_final.drop_duplicates(subset=["Cim"])
        except Exception as e:
            print(f"Hiba a fájl beolvasásakor: {e}")
            df_final = df_new
    else:
        df_final = df_new
        
    df_final.to_excel(file_name, index=False, engine='openpyxl')
    print(f"[{datetime.now()}] Az adatok elmentve az Excelbe.")
    
def job():
    print("Reggeli hírek gyűjtése...")
    news = get_tech_news()
    if news:
        save_to_excel(news)
    
schedule.every().day.at("09:00").do(job)    
        
if __name__ == "__main__":
    print("A Excel Archiváló elindult. Várakozás reggel 9-ig...")
    while True:
        schedule.run_pending()
        time.sleep(60)