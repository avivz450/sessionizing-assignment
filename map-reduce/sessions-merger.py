# Total time and space complexity for merging sessions of constant session files:
# when 'n' is the length of the biggest sessions array that the reducer may receive:
# time complexity - O(nlogn)*(number of visitor id and url couples)
# space complexity - O(n)*(number of visitor id and url couples)

from mrjob.job import MRJob
from mrjob.step import MRStep
import hashlib, csv

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def session_start_compare(self, session):
        return float(session[0])

    # 1 call to this method time and space complexity: O(1)
    # the number of calls to this method is the number of rows in the input files
    # therefore, total hash_strings complexity: O(1)*(number of rows)
    def hash_strings(self, string1, string2):
        key_to_hash = string1 + string2;
        hashed_string =  int(hashlib.sha1(key_to_hash.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        return hashed_string


    # 1 call to this method time and space complexity: O(1)
    # the number of calls to this method is the number of rows in the input files
    # therefore, total mapper complexity: O(1)*(number of rows)
    def mapper(self, _, line):
        data = line.split(',')
        yield self.hash_strings(data[2], data[3]), data

    # In this method we receive a sessions array of a certain visitor id and url
    # this method sorts and groups these sessions when possible
    # when 'n' is the length of a certain sessions array that the reducer receive:
    # 1 call to this method complexity:
    # time complexity - O(nlogn)
    # space complexity - O(n)
    # the number of calls to this method is the number of visitor id and url couples (together)
    # therefore, total reducer time and space complexity:
    # time complexity - O(nlogn)*(number of visitor id and url couples)
    # space complexity - O(n)*(number of visitor id and url couples)
    def reducer(self, _, values):
        sessions = list(values)

        if len(sessions) == 1:
            writer.writerow({'session_length': int(sessions[0][1]) - int(sessions[0][0]) , 'site_url': sessions[0][2], 'visitor_id': sessions[0][3]})
        else:
            sessions.sort(key=self.session_start_compare)

            merged_sessions = []
            start, end, site_url, visitor_id = sessions[0]

            for session in sessions:
                if float(session[0]) <= float(end) + 1800:
                    end = str(max(int(end), int(session[1])))
                else:
                    merged_sessions.append([start, end, site_url, visitor_id])
                    start, end, site_url, visitor_id = session

            merged_sessions.append([start, end, site_url, visitor_id])

            for session in merged_sessions:
                writer.writerow({'session_length': int(session[1]) - int(session[0]), 'site_url': session[2], 'visitor_id': session[3]})


if __name__ == '__main__':
    # Create the output file and write the header row
    with open("./data/final_result.csv", 'w', newline='') as f:
        fieldnames = ['session_length', 'site_url', 'visitor_id']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        MRWordCount.run()