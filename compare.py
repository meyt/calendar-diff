import glob
from os.path import basename

res = {}
headers = ['gregory']

for x in glob.glob('*/*.csv'):
  algoname = '.'.join(basename(x).split('.')[:-1])
  headers.append(algoname)
  with open(x, 'r') as f:
    for line in f:
      src, dst = line.split(',')
      src, dst = src.strip(), dst.strip()
      if src in res:
        res[src].append(dst)
      else:
        res[src] = [dst]

with open('calendar-diff.csv', 'w') as diff_file:
  with open('calendar-all.csv', 'w') as all_file:
    diff_file.write(f'{",".join(headers)}\n')
    all_file.write(f'{",".join(headers)}\n')

    for k, v in res.items():
      line = f'{k},{",".join(v)}\n'
      all_file.write(line)
      if not all([x == v[0] for x in v[1:]]):
        diff_file.write(line)
