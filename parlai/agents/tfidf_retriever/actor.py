#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task
from parlai.utils.logging import logger, ERROR

import os
import unittest

from parlai.agents.tfidf_retriever.tfidf_retriever import (
    TfidfRetrieverAgent,
)

class TfidfRetrieverActor():
    """
    Basic tests on the display_data.py example.
    """
    def __init__(self):
        print('init')

    def run_actor(self):
        MODEL_FILE = '/Volumes/Data/ParlAI/from_pretrained_wiki/wikiqa_tdifd'
        DB_PATH = '/Volumes/Data/ParlAI/from_pretrained_wiki/wikiqa_tdifd.db'
        TFIDF_PATH = '/Volumes/Data/ParlAI/from_pretrained_wiki/wikiqa_tdifd.tfidf'
        # keep things quiet
        logger.setLevel(ERROR)
        parser = ParlaiParser(True, True)
        parser.set_defaults(
            model_file=MODEL_FILE,
            interactive_mode=True,
        )
        opt = parser.parse_args([], print_args=False)
        opt['interactive_mode'] = True
        agent = create_agent(opt)
        train_world = create_task(opt, agent)
        # pass examples to dictionary
        while not train_world.epoch_done():
            train_world.parley()
        agent.observe(obs)
        reply = 'Hello'
        
        return reply