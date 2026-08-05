#!/Users/taraqfarhan/Desktop/programming/gh-repos/quran/.venv/bin/python3
import csv, requests, time

# en.sahih = Saheeh International
# en.yusufali = Yusuf Ali Translation
EDITIONS = "quran-uthmani,en.sahih"
rows = []
for surah in range(1, 115):
    r = requests.get(f"https://api.alquran.cloud/v1/surah/{surah}/editions/{EDITIONS}",
                     timeout=30)
    r.raise_for_status()
    data = r.json()["data"]
    en = data[1]                       # English edition
    for a in en["ayahs"]:
        rows.append({"surah": surah, "ayah": a["numberInSurah"],
                     "verse_key": f"{surah}:{a['numberInSurah']}",
                     "text": a["text"]})
    time.sleep(0.2)

with open("quran_en.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["surah", "ayah", "verse_key", "text"])
    w.writeheader(); w.writerows(rows)

print(f"Wrote {len(rows)} verses")

