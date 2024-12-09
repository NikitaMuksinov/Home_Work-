
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="07052002",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# 1. Показать все произведения данного композитора
def get_works_by_composer(composer_name):
    cursor.execute("""
        SELECT w.title, w.year, w.album, w.genre 
        FROM work w 
        JOIN composer c ON w.composer_id = c.id
        WHERE c.name = %s;
    """, (composer_name,))
    return cursor.fetchall()

# 2. Показать местоположение выбранного произведения
def get_work_location(work_title):
    cursor.execute("""
        SELECT l.location 
        FROM location l 
        JOIN work w ON l.work_id = w.id
        WHERE w.title = %s;
    """, (work_title,))
    return cursor.fetchone()

# 3. Показать список носителей для выбранного произведения
def get_media_for_work(work_title):
    cursor.execute("""
        SELECT m.type 
        FROM media m 
        JOIN work w ON m.work_id = w.id
        WHERE w.title = %s;
    """, (work_title,))
    return cursor.fetchall()

# 4. Показать список произведений по жанру исполнения
def get_works_by_genre(genre):
    cursor.execute("""
        SELECT w.title, w.year, w.album 
        FROM work w 
        WHERE w.genre = %s;
    """, (genre,))
    return cursor.fetchall()

# 5. Найти произведение по названию, году выпуска, альбому
def find_work(title=None, year=None, album=None):
    query = "SELECT * FROM work WHERE TRUE"
    params = []
    if title:
        query += " AND title = %s"
        params.append(title)
    if year:
        query += " AND year = %s"
        params.append(year)
    if album:
        query += " AND album = %s"
        params.append(album)
    cursor.execute(query, params)
    return cursor.fetchall()

# 6. Список произведений композитора по годам
def get_works_by_composer_and_years(composer_name, start_year, end_year):
    cursor.execute("""
        SELECT w.title, w.year 
        FROM work w 
        JOIN composer c ON w.composer_id = c.id
        WHERE c.name = %s AND w.year BETWEEN %s AND %s;
    """, (composer_name, start_year, end_year))
    return cursor.fetchall()

# Пример вызова функций
print(get_works_by_composer("Ludwig van Beethoven"))
print(get_work_location("Symphony No. 9"))
print(get_media_for_work("Hey Jude"))
print(get_works_by_genre("Classical"))
print(find_work(title="Hey Jude", year=1968))
print(get_works_by_composer_and_years("The Beatles", 1960, 1970))

# Закрытие соединения
cursor.close()
conn.close()