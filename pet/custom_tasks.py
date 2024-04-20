# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
To add a new task to PET, both a DataProcessor and a PVP for this task must
be added. The DataProcessor is responsible for loading training and test data.
This file shows an example of a DataProcessor for a new task.
"""

import csv
import os
import pandas as pd
from typing import List

from pet.task_helpers import MultiMaskTaskHelper
from pet.tasks import DataProcessor, PROCESSORS, TASK_HELPERS
from pet.utils import InputExample
from abc import ABC, abstractmethod


class HaddassahRHsexDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "sex"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["m", "f", "unknown"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "sex"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHimmigrantDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "immigrant"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "immigrant"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHmarital_statusDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "marital_status"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["married", "not_married", "unknown"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "marital_status"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples


class HaddassahRHchildrenDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "children"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no", "unknown"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "children"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHclosest_relativeDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "closest_relative"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["at_home", "close", "far", "unknown"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "closest_relative"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHclosest_supporting_relativeDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "closest_supporting_relative"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["at_home", "close", "far", "unknown"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "closest_supporting_relative"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples


class HaddassahRHseeking_help_at_homeDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "seeking_help_at_home"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "seeking_help_at_home"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHis_holocaust_survivorDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "is_holocaust_survivor"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "is_holocaust_survivor"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHis_exhaustedDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "is_exhausted"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "is_exhausted"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHneeds_extreme_nursingDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "needs_extreme_nursing"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "needs_extreme_nursing"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHhas_extreme_nursingDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "has_extreme_nursing"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "has_extreme_nursing"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHis_confusedDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "is_confused"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "is_confused"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples



class HaddassahRHis_dementicDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "is_dementic"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["yes", "no"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "is_dementic"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples


class HaddassahRHresidenceDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "residence"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["home", "nursing_home"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "residence"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples


class HaddassahRHrecommended_residenceDataProcessor(DataProcessor):

    # Set this to the name of the task
    TASK_NAME = "recommended_residence"
    gets_args = True

    def __init__(self, args):
        super().__init__()

        self.TRAIN_FILE_NAME = "train.tsv"
        self.DEV_FILE_NAME = "dev.tsv"
        self.TEST_FILE_NAME = "test.tsv"
        self.UNLABELED_FILE_NAME = "unlabeled.tsv"
        self.LABELS = ["home", "nursing_home"]
        self.TEXT_A_COLUMN = "social_assesment" if not args.hebrew else "social_assesment_hebrew"
        self.TEXT_B_COLUMN = -1
        self.LABEL_COLUMN = "recommended_residence"

    def get_train_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TRAIN_FILE_NAME), "train")

    def get_dev_examples(self, data_dir: str) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.DEV_FILE_NAME), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.TEST_FILE_NAME), "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, self.UNLABELED_FILE_NAME), "unlabeled")

    def get_labels(self) -> List[str]:
        return self.LABELS

    def _create_examples(self, path, set_type, max_examples=-1, skip_first=0):
        examples = []

        with open(path) as f:
            df = pd.read_csv(f.name, delimiter='\t', dtype=str)
            df = df.reset_index()

            for idx, row in df.iterrows():
                guid = "%s-%s" % (set_type, idx)
                label = row[self.LABEL_COLUMN]
                text_a = row[self.TEXT_A_COLUMN]
                text_b = row[self.TEXT_B_COLUMN] if self.TEXT_B_COLUMN >= 0 else None
                example = InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label)
                examples.append(example)

        return examples


PROCESSORS[HaddassahRHsexDataProcessor.TASK_NAME.lower()] = HaddassahRHsexDataProcessor
PROCESSORS[HaddassahRHimmigrantDataProcessor.TASK_NAME.lower()] = HaddassahRHimmigrantDataProcessor
PROCESSORS[HaddassahRHmarital_statusDataProcessor.TASK_NAME.lower()] = HaddassahRHmarital_statusDataProcessor
PROCESSORS[HaddassahRHchildrenDataProcessor.TASK_NAME.lower()] = HaddassahRHchildrenDataProcessor
PROCESSORS[HaddassahRHclosest_relativeDataProcessor.TASK_NAME.lower()] = HaddassahRHclosest_relativeDataProcessor
PROCESSORS[HaddassahRHclosest_supporting_relativeDataProcessor.TASK_NAME.lower()] = HaddassahRHclosest_supporting_relativeDataProcessor
PROCESSORS[HaddassahRHseeking_help_at_homeDataProcessor.TASK_NAME.lower()] = HaddassahRHseeking_help_at_homeDataProcessor
PROCESSORS[HaddassahRHis_holocaust_survivorDataProcessor.TASK_NAME.lower()] = HaddassahRHis_holocaust_survivorDataProcessor
PROCESSORS[HaddassahRHis_exhaustedDataProcessor.TASK_NAME.lower()] = HaddassahRHis_exhaustedDataProcessor
PROCESSORS[HaddassahRHneeds_extreme_nursingDataProcessor.TASK_NAME.lower()] = HaddassahRHneeds_extreme_nursingDataProcessor
PROCESSORS[HaddassahRHhas_extreme_nursingDataProcessor.TASK_NAME.lower()] = HaddassahRHhas_extreme_nursingDataProcessor
PROCESSORS[HaddassahRHis_confusedDataProcessor.TASK_NAME.lower()] = HaddassahRHis_confusedDataProcessor
PROCESSORS[HaddassahRHis_dementicDataProcessor.TASK_NAME.lower()] = HaddassahRHis_dementicDataProcessor
PROCESSORS[HaddassahRHresidenceDataProcessor.TASK_NAME.lower()] = HaddassahRHresidenceDataProcessor
PROCESSORS[HaddassahRHrecommended_residenceDataProcessor.TASK_NAME.lower()] = HaddassahRHrecommended_residenceDataProcessor
