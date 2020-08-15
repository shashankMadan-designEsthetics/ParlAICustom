from parlai.scripts.display_data import DisplayData
# DisplayData.main(task='wikiqa', num_examples=5)

from parlai.scripts.display_model import DisplayModel
DisplayModel.main(
    task='bankQA',
    model_file='from_pretrained/model',
    num_examples=10,
    skip_generation=False,
)

# from parlai.scripts.train_model import TrainModel

# print(TrainModel.help(model='seq2seq'))