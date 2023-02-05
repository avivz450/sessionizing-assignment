# Total complexity of script
# O(values)*(number of keys of visitor id and url)

from mrjob.job import MRJob
from mrjob.step import MRStep
import hashlib, csv, sys

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    # O(1) - memory + time
    def hash_strings(self, string1, string2):
        key_to_hash = string1 + string2;
        hashed_string =  int(hashlib.sha1(key_to_hash.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        return hashed_string

    # O(1) - memory + time
    # O(1)*number_of_lines
    def mapper(self, _, line):
       data = line.split(',')
       yield self.hash_strings(data[0], data[1]), data

    # O(values) - memory + time complexity
    # O(values)*(number of keys of visitor id and url)
    def reducer(self, key, values):
        page_views_list = list(values)
        sessions = []
        last_session = None

        for page_view in page_views_list:
            if not last_session or (float(page_view[3]) - float(last_session[1])) > 1800:
                last_session = [page_view[3], page_view[3], page_view[1], page_view[0]]
                sessions.append(last_session)
            else:
                last_session[1] = page_view[3]

        for session in sessions:
            writer.writerow({'start': session[0], 'end': session[1], 'site_url': session[2], 'visitor_id': session[3]})



if __name__ == '__main__':
    # Create the output file and write the header row
    with open(sys.argv[1].replace('input', 'output'), 'w', newline='') as f:
        fieldnames = ['start', 'end', 'site_url', 'visitor_id']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        MRWordCount.run()