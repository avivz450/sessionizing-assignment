# Total time and space complexity for creating sessions of an input file:
# O(n)*(number of visitor id and url couples), when n = page views array length

from mrjob.job import MRJob
from mrjob.step import MRStep
import hashlib, csv, sys

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    # 1 call to this method time and space complexity: O(1)
    # the number of calls to this method is the number of rows in the input file
    # therefore, total hash_strings complexity: O(1)*(number of rows)
    def hash_strings(self, string1, string2):
        key_to_hash = string1 + string2;
        hashed_string =  int(hashlib.sha1(key_to_hash.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        return hashed_string

    # 1 call to this method time and space complexity: O(1)
    # the number of calls to this method is the number of rows in the input file
    # therefore, total mapper complexity: O(1)*(number of rows)
    def mapper(self, _, line):
       data = line.split(',')
       yield self.hash_strings(data[0], data[1]), data

    # In this method we have a sorted by timestamp page views array, of a certain visitor id and url
    # This method groups these page views into sessions
    # 1 call to this method time and space complexity:
    # O(page views array length)
    # the number of calls to this method is the number of visitor id and url couples (together)
    # therefore, total reducer time and space complexity:
    # O(page views array length)*(number of visitor id and url couples)
    def reducer(self, _, values):
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