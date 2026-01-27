TechPulse Archiver - Automated News Data Engineering

A TechPulse Archiver egy autonóm Python-alapú mikroszolgáltatás, amely napi szinten aggregál technológiai híreket a Hacker News-ról, és azokat egy strukturált Excel adatbázisba archiválja. A projekt célja egy skálázható adatgyűjtő folyamat bemutatása, amely emberi beavatkozás nélkül fut.


Funkciók:
- Web Scraping: Automatizált adatnyerés BeautifulSoup4 és Requests könyvtárakkal
- Intelligens adatkezelés: A Pandas könyvtár használatával történő adatfeldolgozás és duplikációszűrés
- Persistent Storage: Hosszú távú adattárolás Excel formátumban
- Autonomous Scheduling: Beépített időzítő mechanizmus, amely minden nap reggel 09:00-kor elindítja a folyamatot
- Always-on Architecture: Docker-konténerbe zárt futtathatóság (```restart: always``` logikával)

Technológiai Stack:
- Language: Python
- Data Processing: Pandas
- Scraping: BeautifulSoup4
- Scheduling: Schedule könyvtár
- Environment: Docker és Docker Compose (időzóna szinkronizációval)


Gyorsindítás:
1. Repo clone
git clone https://github.com/username/techpulse-archiver.git
cd techpulse-archiver

2. Indítás
docker compose up -d


Fejlesztés közbeni kihívások és megfontolások:
1. Adatkonzisztencia és duplikáció:
A legnagyobb kihívást az ismétlődő hírek kezelése jelentette. Megoldásként a Pandas ```drop_duplicates``` funkcióját alkalmaztam a hírek címei alapján, így az archívum csak egyedi bejegyzéseket tartalmaz, függetlenül attól, hogy egy hír hány napig szerepel a címlapon.

2. Bot-védelem megkerülése:
Sok weboldal blokkolja a script-alapú kéréseket. A szoftverbe beépítettem egy egyedi User-Agent fejlécet, amely szimulálja a modern böngészőket, biztosítva a zavartalan adatgyűjtést.

3. Docker időzóna kezelés:
Konténeres környezetben az alapértelmezett UTC időzóna miatt az időzítés eltolódhatott volna. Ezért a Dockerfile-ban implementáltam a ```TZ=Europe/Budapest``` beállítást, hogy az időzítés pontosan a helyi időszerint 09:00-kor történjen.


Struktúra:
.
├── main.py                     # A fő alkalmazáslogika
├── tech_hirek_archivum.xlsx    # Az automatikusan generált adatbázis
├── Dockerfile                  # Konténer definíció (Timezone configgal)
├── docker-compose.yml          # Orchestration (Volumes & Restart policy)
└── requirements.txt            # Szükséges Python könyvtárak

Készítette: Molnár Gergő - https://www.linkedin.com/in/gerg%C5%91-moln%C3%A1r-3920b53a7/
