import json

from parlai.core.teachers import register_teacher, DialogTeacher
from parlai.scripts.display_data import DisplayData

@register_teacher("bankQA")
class DefaultTeacher(DialogTeacher):
    def __init__(self, opt, shared=None):
        # opt is the command line arguments.

        # What is this shared thing?
        # We make many copies of a teacher, one-per-batchsize. Shared lets us store

        # We just need to set the "datafile".  This is boilerplate, but differs in many teachers.
        # The "datafile" is the filename where we will load the data from. In this case, we'll set it to
        # the fold name (train/valid/test) + ".txt"
        opt['datafile'] = 'train.json'
        super().__init__(opt, shared)

    def setup_data(self, datafile):
        # filename tells us where to load from.
        # We'll just use some hardcoded data, but show how you could read the filename here:
        print(f" ~~ Loading from {datafile} ~~ ")

        with open(datafile) as f:
                data = json.load(f)
                for d in data:
                    yield (d['text'], d['labels'], d['knowledge']), True