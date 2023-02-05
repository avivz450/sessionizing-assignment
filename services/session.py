import subprocess
import glob

class SessionService:
    DATA_PATH = "./data/"
    SESSIONS_CREATOR_PATH = "./map-reduce/sessions-creator.py"
    SESSIONS_MERGER_PATH = "./map-reduce/sessions-merger.py"

    def create_sessions_data(self):
        mapreduce_inputs = glob.glob(self.DATA_PATH + 'input_*')
        for mapreduce_input in mapreduce_inputs:
            subprocess.run(["python", self.SESSIONS_CREATOR_PATH, mapreduce_input])

        merge_sessions_command = ["python", self.SESSIONS_MERGER_PATH]

        mapreduce_outputs = glob.glob(self.DATA_PATH + 'output_*')

        for output in mapreduce_outputs:
            merge_sessions_command.append(output)

        subprocess.run(merge_sessions_command)