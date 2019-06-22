js_playlist = {
    'title' : 'New Favorite Songs',
    'author' : 'Jeanne',
    'songs' : [
        {
            'title' : 'Worship',
            'artists' : ['Lizzo'],
            'playlist_track_num' : 1,
            'genres' : ['pop', 'soul'],
            'duration' : 3.7
        },
        {
            'title' : 'Trouble',
            'artists' : ['Izzy', 'Jennifer Hudson'],
            'playlist_track_num' : 2,
            'genres' : ['pop', 'soul'],
            'duration' : 4.0
        }
    ]
}
print(js_playlist)

total = 0.0
for song in js_playlist['songs']:
    total += song['duration']

print(total)
