from sys import argv
import csv


front_matter = '''<?xml version="1.0" encoding="UTF-8"?>
<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">
'''


back_matter = '''
<d:entry id="front_back_matter" d:title="書面">
  <h1><b>廣韻</b></h1>
  <div>
    鍵入漢字以得其音。<br/>
  </div>
  <p><img src="Images/Book.png"/></p>
</d:entry>
</d:dictionary>
'''


def collect_entries(raw_path):
    entries = {}
    with open(raw_path, 'r') as f:
        next(f) # skip head
        # 20: 反切
        # 24: 字頭
        # 25: 釋義
        # 30~34: 聲紐 呼 等 韻部 調
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for entry in reader:
            pyanchet, zy, qrie, sjeqnriw, hu, toq, xwnbu, dew = entry[20], entry[24], entry[25], *entry[30:35]
            record = {
                'pyanchet': pyanchet,
                'qrie': qrie,
                'sjeqnriw': sjeqnriw,
                'hu': hu,
                'toq': toq,
                'xwnbu': xwnbu,
                'dew': dew
            }
            if zy not in entries:
                entries[zy] = [record]
            else:
                entries[zy].append(record)
    return entries


def main(raw_path, output_path):
    with open(output_path, 'w') as f:
        f.write(front_matter)
        entries = collect_entries(raw_path)
        for zy, priew in entries.items():
            f.write('<d:entry id="{id}" d:title="{title}">\n'.format(id=zy, title=zy))
            f.write(' <d:index d:value="{}"/>\n'.format(zy))
            for dow in priew:
                f.write(' <h2>{}切</h2>'.format(dow['pyanchet']))
                f.write(' <p>{}{}{}{}{}</p>'.format(dow['sjeqnriw'], dow['toq'], dow['hu'], dow['xwnbu'], dow['dew']))
                f.write(' <p>{}</p>'.format(dow['qrie']))
                f.write('<br/>\n')
            f.write('</d:entry>\n')
        f.write(back_matter)


if __name__ == '__main__':
    main(argv[1], argv[2])
