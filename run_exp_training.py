from parlai.scripts.train_model import TrainModel

TrainModel.main(
    # similar to before
    task='bankQA',
    model='projects.wizard_of_wikipedia.generator.agents:EndToEndAgent',
    model_file='/from_pretrained_wiki/model',
    # initialize with a pretrained model
    init_model='zoo:wizard_of_wikipedia/end2end_generator/model',

    # arguments we get from the pretrained model.
    # Unfortunately, these must be looked up separately for each model.
    # eps
    dict_file='zoo:wizard_of_wikipedia/end2end_generator/model.dict',
    num_epochs=2,
    dict_lower=True,
    dict_tokenizer='bpe',
    n_layers=5,
    n_heads=2,
    dropout=0.20,
    ffn_size=512,
    embedding_size=256,
    log_every_n_secs=10,
    validation_patience=12,
    validation_metric='ppl',
    validation_metric_mode='min',
    validation_every_n_epochs=0.5,
    n_positions=128,
    truncate=128,
    max_knowledge=32,
    knowledge_alpha=0.95,
    knowledge_truncate=32,
    learningrate=5e-4,
    warmup_updates=5000,
    clip=0.1,
    lr_scheduler='invsqrt',
    embedding_type='fasttext',
    beam_size=1,
    skip_generation=False,
    batchsize=64,
    # fp16=True
)