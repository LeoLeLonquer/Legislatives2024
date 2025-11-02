#!/usr/bin/env python

import requests


def download(url, filepath):
    r = requests.get(url, stream=True)

    with open('data.txt', 'w') as f:
        for chunk in r.iter_content(chunk_size=16*1024):
            f.write(chunk)
    f.close()


url = "https://www.data.gouv.fr/api/1/datasets/r/f98165a7-7c37-4705-a181-bcfc943edc73"
filepath = "contours/contours-france-entiere-latest-v2.geojson"
download(url, filepath)

url = "https://www.data.gouv.fr/api/1/datasets/r/6813fb28-7ec0-42ff-a528-2bc3d82d7dcd"
filepath = "bureaux_scores/France/resultats-definitifs-par-bureau-de-vote-tour1.csv"
download(url, filepath)

url = "https://www.data.gouv.fr/api/1/datasets/r/ca974f04-cfd9-4da8-8554-4a868a09c6c2"
filepath = "bureaux_scores/France/resultats-definitifs-par-bureau-de-vote-tour2.csv"
download(url, filepath)
