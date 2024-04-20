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
be added. The PVP is responsible for applying patterns to inputs and mapping
labels to their verbalizations (see the paper for more details on PVPs).
This file shows an example of a PVP for a new task.
"""

from typing import List

from pet.pvp import PVP, PVPS
from pet.utils import InputExample


class HaddassahRHsexPVP(PVP):

    TASK_NAME = "sex"

    VERBALIZER_A = {
        "m": ["yes"],
        "f": ["no"],
        "unknown": ["maybe"],
    }
    VERBALIZER_B = {
        "m": ["yes"],
        "f": ["no"],
        "unknown": ["maybe"],
    }
    VERBALIZER_C = {
        "m": ["male"],
        "f": ["female"],
        "unknown": ["unknown"],
    }
    VERBALIZER_D = {
        "m": ["man"],
        "f": ["woman"],
        "unknown": ["unknown"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'is this person a man?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'is this person a male?', self.mask], []
        elif self.pattern_id == 2:
            return [text_a, "this person's sex is <mask>?", self.mask], []
        elif self.pattern_id == 3:
            return [text_a, "this person's gender is <mask>?", self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHsexPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHsexPVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHsexPVP.VERBALIZER_C[label]
        elif self.pattern_id == 3:
            return HaddassahRHsexPVP.VERBALIZER_D[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHimmigrantPVP(PVP):

    TASK_NAME = "immigrant"

    VERBALIZER_A = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_B = {
        "yes": ["outside"],
        "no": ["inside"],
    }
    VERBALIZER_C = {
        "yes": ["far"],
        "no": ["here"],
    }
    VERBALIZER_D = {
        "yes": ["far"],
        "no": ["here"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'is this person an immigrant?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'this person was born', self.mask, 'Israel'], []
        elif self.pattern_id == 2:
            return [text_a, 'this person was born', self.mask], []
        elif self.pattern_id == 3:
            return [text_a, 'this person is from', self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHimmigrantPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHimmigrantPVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHimmigrantPVP.VERBALIZER_C[label]
        elif self.pattern_id == 3:
            return HaddassahRHimmigrantPVP.VERBALIZER_D[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHmarital_statusPVP(PVP):

    TASK_NAME = "marital_status"

    VERBALIZER_A = {
        "married": ["yes"],
        "not_married": ["no"],
        "unknown": ["maybe"],
    }
    VERBALIZER_B = {
        "married": ["married"],
        "not_married": ["single"],
        "unknown": ["alone"],
    }
    VERBALIZER_C = {
        "married": ["married"],
        "not_married": ["single"],
        "unknown": ["alone"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, "is this person married?", self.mask], []
        elif self.pattern_id == 1:
            return [text_a, "this person is", self.mask], []
        elif self.pattern_id == 2:
            return ["this person is", self.mask, ": ", text_a], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHmarital_statusPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHmarital_statusPVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHmarital_statusPVP.VERBALIZER_C[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHchildrenPVP(PVP):

    TASK_NAME = "children"

    VERBALIZER_A = {
        "yes": ["yes"],
        "no": ["no"],
        "unknown": ["maybe"],
    }
    VERBALIZER_B = {
        "yes": ["yes"],
        "no": ["no"],
        "unknown": ["maybe"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'does this person have children?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'does this person have kids?', self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHchildrenPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHchildrenPVP.VERBALIZER_B[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHclosest_relativePVP(PVP):

    TASK_NAME = "closest_relative"

    VERBALIZER_A = {
        "at_home": ["with"],
        "close": ["close"],
        "far": ["far"],
        "unknown": ["alone"],
    }
    VERBALIZER_B = {
        "at_home": ["with"],
        "close": ["close"],
        "far": ["far"],
        "unknown": ["alone"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, "this person's relatives live", self.mask], []
        elif self.pattern_id == 1:
            return [text_a, "this person lives", self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHclosest_relativePVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHclosest_relativePVP.VERBALIZER_B[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHclosest_supporting_relativePVP(PVP):

    TASK_NAME = "closest_supporting_relative"

    VERBALIZER_A = {
        "at_home": ["home"],
        "close": ["close"],
        "far": ["far"],
        "unknown": ["alone"],
    }
    VERBALIZER_B = {
        "at_home": ["home"],
        "close": ["close"],
        "far": ["far"],
        "unknown": ["alone"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, "this person's relatives support them from", self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'this person is aided by their relatives from', self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHclosest_supporting_relativePVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHclosest_supporting_relativePVP.VERBALIZER_B[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHseeking_help_at_homePVP(PVP):

    TASK_NAME = "seeking_help_at_home"

    VERBALIZER_A = {
        "yes": ["need"],
        "no": ["has"],
    }
    VERBALIZER_B = {
        "yes": ["want"],
        "no": ["has"],
    }
    VERBALIZER_C = {
        "yes": ["ask"],
        "no": ["has"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'this person', self.mask, 'more help hours than others'], []
        elif self.pattern_id == 1:
            return [text_a, 'this person', self.mask, 'more help hours than others'], []
        elif self.pattern_id == 2:
            return [text_a, 'this person', self.mask, 'more help hours than others'], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHseeking_help_at_homePVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHseeking_help_at_homePVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHseeking_help_at_homePVP.VERBALIZER_C[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))




class HaddassahRHis_holocaust_survivorPVP(PVP):

    TASK_NAME = "is_holocaust_survivor"

    VERBALIZER_A = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_B = {
        "yes": ["yes"],
        "no": ["no"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'is this person a holocaust survivor?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'has this person lived trough the holocaust?', self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHis_holocaust_survivorPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHis_holocaust_survivorPVP.VERBALIZER_B[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))




class HaddassahRHis_exhaustedPVP(PVP):

    TASK_NAME = "is_exhausted"

    VERBALIZER_A = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_B = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_C = {
        "yes": ["yes"],
        "no": ["no"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'is this person exhausted?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'is this person fatigued?', self.mask], []
        elif self.pattern_id == 2:
            return [text_a, "is this person debilitated?", self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHis_exhaustedPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHis_exhaustedPVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHis_exhaustedPVP.VERBALIZER_C[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))




class HaddassahRHneeds_extreme_nursingPVP(PVP):

    TASK_NAME = "needs_extreme_nursing"

    VERBALIZER_A = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_B = {
        "yes": ["seek"],
        "no": ["avoid"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'does this person need nursing?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'this person should', self.mask, '<mask> nursing'], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHneeds_extreme_nursingPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHneeds_extreme_nursingPVP.VERBALIZER_B[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))




class HaddassahRHhas_extreme_nursingPVP(PVP):

    TASK_NAME = "has_extreme_nursing"

    VERBALIZER_A = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_B = {
        "yes": ["has"],
        "no": ["needs"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'does this person have nursing?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'this person', self.mask, '<mask> nursing'], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHhas_extreme_nursingPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHhas_extreme_nursingPVP.VERBALIZER_B[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHis_confusedPVP(PVP):

    TASK_NAME = "is_confused"

    VERBALIZER_A = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_B = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_C = {
        "yes": ["yes"],
        "no": ["no"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'is this person confused?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'is this person disoriented?', self.mask], []
        elif self.pattern_id == 2:
            return [text_a, "is this person forgetful?", self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHis_confusedPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHis_confusedPVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHis_confusedPVP.VERBALIZER_C[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHis_dementicPVP(PVP):

    TASK_NAME = "is_dementic"

    VERBALIZER_A = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_B = {
        "yes": ["yes"],
        "no": ["no"],
    }
    VERBALIZER_C = {
        "yes": ["yes"],
        "no": ["no"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'does this person suffer from dementia?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'is this person mentally ill?', self.mask], []
        elif self.pattern_id == 2:
            return [text_a, "does this person have alzheimer's?", self.mask], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHis_dementicPVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHis_dementicPVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHis_dementicPVP.VERBALIZER_C[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))




class HaddassahRHresidencePVP(PVP):

    TASK_NAME = "residence"

    VERBALIZER_A = {
        "home": ["yes"],
        "nursing_home": ["no"],
    }
    VERBALIZER_B = {
        "home": ["no"],
        "nursing_home": ["yes"],
    }
    VERBALIZER_C = {
        "home": ["private"],
        "nursing_home": ["rest"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'does this person live in their own home?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'does this person live in a nursing home?', self.mask], []
        elif self.pattern_id == 2:
            return [text_a, "this person lives in a", self.mask, "home"], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHresidencePVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHresidencePVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHresidencePVP.VERBALIZER_C[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


class HaddassahRHrecommended_residencePVP(PVP):

    TASK_NAME = "recommended_residence"

    VERBALIZER_A = {
        "home": ["yes"],
        "nursing_home": ["no"],
    }
    VERBALIZER_B = {
        "home": ["no"],
        "nursing_home": ["yes"],
    }
    VERBALIZER_C = {
        "home": ["private"],
        "nursing_home": ["rest"],
    }

    def get_parts(self, example: InputExample):

        text_a = self.shortenable(example.text_a)
        text_b = self.shortenable(example.text_b)

        if self.pattern_id == 0:
            return [text_a, 'should this person live in their own home?', self.mask], []
        elif self.pattern_id == 1:
            return [text_a, 'should this person live in a nursing home?', self.mask], []
        elif self.pattern_id == 2:
            return [text_a, "this person should live in a", self.mask, "home"], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        if self.pattern_id == 0:
            return HaddassahRHrecommended_residencePVP.VERBALIZER_A[label]
        elif self.pattern_id == 1:
            return HaddassahRHrecommended_residencePVP.VERBALIZER_B[label]
        elif self.pattern_id == 2:
            return HaddassahRHrecommended_residencePVP.VERBALIZER_C[label]
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))


PVPS[HaddassahRHsexPVP.TASK_NAME.lower()] = HaddassahRHsexPVP
PVPS[HaddassahRHimmigrantPVP.TASK_NAME.lower()] = HaddassahRHimmigrantPVP
PVPS[HaddassahRHmarital_statusPVP.TASK_NAME.lower()] = HaddassahRHmarital_statusPVP
PVPS[HaddassahRHchildrenPVP.TASK_NAME.lower()] = HaddassahRHchildrenPVP
PVPS[HaddassahRHclosest_relativePVP.TASK_NAME.lower()] = HaddassahRHclosest_relativePVP
PVPS[HaddassahRHclosest_supporting_relativePVP.TASK_NAME.lower()] = HaddassahRHclosest_supporting_relativePVP
PVPS[HaddassahRHseeking_help_at_homePVP.TASK_NAME.lower()] = HaddassahRHseeking_help_at_homePVP
PVPS[HaddassahRHis_holocaust_survivorPVP.TASK_NAME.lower()] = HaddassahRHis_holocaust_survivorPVP
PVPS[HaddassahRHis_exhaustedPVP.TASK_NAME.lower()] = HaddassahRHis_exhaustedPVP
PVPS[HaddassahRHneeds_extreme_nursingPVP.TASK_NAME.lower()] = HaddassahRHneeds_extreme_nursingPVP
PVPS[HaddassahRHhas_extreme_nursingPVP.TASK_NAME.lower()] = HaddassahRHhas_extreme_nursingPVP
PVPS[HaddassahRHis_confusedPVP.TASK_NAME.lower()] = HaddassahRHis_confusedPVP
PVPS[HaddassahRHis_dementicPVP.TASK_NAME.lower()] = HaddassahRHis_dementicPVP
PVPS[HaddassahRHresidencePVP.TASK_NAME.lower()] = HaddassahRHresidencePVP
PVPS[HaddassahRHrecommended_residencePVP.TASK_NAME.lower()] = HaddassahRHrecommended_residencePVP
