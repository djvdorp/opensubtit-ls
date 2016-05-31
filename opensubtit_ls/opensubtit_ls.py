from pythonopensubtitles.opensubtitles import OpenSubtitles
from tabulate import tabulate
from datetime import datetime
import argparse
import re

def main():
    parser = argparse.ArgumentParser(description="List available subtitles for a show")
    parser.add_argument("show", help="Show you want to list the subtitles for")
    parser.add_argument("-s", "--season", help="Season you want to list", type=int, default=1)
    parser.add_argument("-l", "--language", help="Language you want to list subtitles in", default='en')
    args = parser.parse_args()

    os = OpenSubtitles()
    os.login(username=None, password=None)

    show_name = args.show
    sub_language = args.language
    season = str(args.season)

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

if __name__ == '__main__':
    main()