from pythonopensubtitles.opensubtitles import OpenSubtitles
from tabulate import tabulate
from datetime import datetime
import re

sub_language = 'dut'
show_name = 'Suits'
season = '4'

if __name__ == '__main__':
    os = OpenSubtitles()
    os.login(username=None, password=None)

    results = os.search_subtitles([{'sublanguageid': sub_language, 'query': show_name, 'season': season}])
    sorted_results = sorted(results, key=lambda x: int(x['SeriesEpisode']))

    table = []
    for result in sorted_results:
        name = result['MovieName'].strip()
        match_exact_show_name_regex = r'\"{}\"'.format(show_name)
        if re.search(match_exact_show_name_regex, name):
            username_raw = result['UserNickName']
            username = username_raw if username_raw else 'nobody'
            size = result['SubSize']
            date_raw = result['SubAddDate']
            date = datetime.strptime(date_raw, '%Y-%m-%d %H:%M:%S')
            filename = result['SubFileName']
            table.append(['-r--r--r--', '1', username, username, size,
                          date.strftime('%b %d %H:%M'), filename])

    print "total {}".format(len(table))
    print tabulate(table, tablefmt="plain")
