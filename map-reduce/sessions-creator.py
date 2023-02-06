# Total time and space complexity for creating sessions of an input file,
# when n = biggest page views array length that the reducer can get
# O(n)*(number of visitor id and url couples)

from mrjob.job import MRJob
from mrjob.step import MRStep
import hashlib, csv, sys

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    # this method maps the data by the visitor id and site url couple
    # 1 call to this method time and space complexity: O(1)
    # the number of calls to this method is the number of rows in the input file
    # therefore, total mapper complexity: O(1)*(number of rows)
    def mapper(self, _, line):
       data = line.split(',')
       yield data[0]+data[1], data

    # In this method we receive a sorted by timestamp page views array, of a certain visitor id and url
    # This method groups these page views into sessions
    # 1 call to this method time and space complexity:
    # O(page views array length)
    # the number of calls to this method is the number of visitor id and url couples (together)
    # therefore, total reducer time and space complexity:
    # O(n)*(number of visitor id and url couples), when n = biggest page views array length that the reducer can get
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