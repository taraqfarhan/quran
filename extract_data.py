#!/usr/bin/env python3
import csv, requests, time
from os import path

# === UPDATE HERE ===
"""
    en.sahih = Saheeh International
    en.yusufali = Yusuf Ali Translation
    en.pickthall = Pickthall Translation
    en.shakir = Shakir Translation
    en.ahmedali = Ahmed Ali Translation
    en.qaribullah = Qaribullah Translation
    en.hilali = Hilali Translation
    en.sarwar = Sarwar Translation
    en.maududi = Maududi Translation
"""
# you can change the editions here, but make sure to keep "quran-uthmani" as the first edition
# for example, you can use EDITIONS = "quran-uthmani,en.yusufali" 
# to get the Yusuf Ali translation instead of Saheeh International
EDITIONS = "quran-uthmani,en.sahih"   

# you can change the output file path here
# you may use FILE_PATH = path.expanduser("~/.quran/data/quran_en.csv")
FILE_PATH = path.expanduser("quran_en.csv") 

# === END OF UPDATE ===

rows = []
for surah in range(1, 115):
    r = requests.get(f"https://api.alquran.cloud/v1/surah/{surah}/editions/{EDITIONS}",timeout=30)
    r.raise_for_status()
    data = r.json()["data"]
    en = data[1]                       # English edition
    for a in en["ayahs"]:
        rows.append(
            {
                "surah": surah,
                "ayah": a["numberInSurah"],
                "verse_key": f"{surah}:{a['numberInSurah']}",
                "text": a["text"]
            }
        )
    time.sleep(0.2)

with open(FILE_PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["surah", "ayah", "verse_key", "text"])
    w.writeheader(); w.writerows(rows)

print(f"Wrote {len(rows)} verses to {FILE_PATH}")
