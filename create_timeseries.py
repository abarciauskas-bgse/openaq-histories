import csv
import re
import io, json
import datetime

cities = ['San_Francisco', 'Los_Angeles-N.Mai', 'Portland-SE_Lafaye', 'Seattle-Beacon_Hill']

for city in cities:
  with open(f'{city}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    ts = []
    date_regex = r'local=(.+)-\d{2}:\d{2}'
    for row in csv_reader:
      if line_count == 0:
        line_count += 1
      else:
        matches = re.search(date_regex, row[0])
        datetime_str = matches.group(1)
        timestamp = datetime.datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S").timestamp()*1000
        ts.append([int(timestamp), float(row[3])])
        line_count += 1
    with io.open(f'{city}.json', 'w', encoding='utf-8') as f:
      f.write(json.dumps(ts, ensure_ascii=False, indent=2))
    print(f'Wrote file {city}.json')
    print(f'Processed {line_count} lines.')
