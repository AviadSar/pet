import os


slurm_config_string = \
'#!/bin/bash\n\
#SBATCH --mem=16g\n\
#SBATCH --gres=gpu:rtx2080\n\
#SBATCH --time=48:0:0\n\
#SBATCH --output=/cs/labs/roys/aviadsa/pet/slurm_out_files/{1}_{0}.txt\n\
#SBATCH --killable\n\
\n\
python3 cli.py --method {1} --pattern_ids {2} --data_dir "/cs/labs/roys/aviadsa/datasets/HaddassahRH" --model_type {3} --model_name_or_path "{4}" --task_name {0} --output_dir "outputs/{1}_{0}" --do_train --do_eval --overwrite_output_dir --pet_max_seq_length 256 --sc_max_seq_length 256'

run_string = 'sbatch {0} >> slurm_configs/submitted_jobs.txt && truncate -s-1 slurm_configs/submitted_jobs.txt && echo -n " sbatch {0}\n" >> slurm_configs/submitted_jobs.txt\n'

slurm_dir = '/cs/labs/roys/aviadsa/pet/slurm_configs'


file_name = 'sex'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2 3',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'immigrant'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2 3',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'marital_status'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'closest_relative'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'closest_supporting_relative'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'seeking_help_at_home'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'is_holocaust_survivor'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'is_exhausted'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'needs_extreme_nursing'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'has_extreme_nursing'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'is_confused'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'is_dementic'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'residence'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'recommended_residence'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'ipet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


# file_name = 'sex'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2 3',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'immigrant'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2 3',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'marital_status'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'children'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'closest_relative'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'closest_supporting_relative'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'seeking_help_at_home'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'is_holocaust_survivor'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'is_exhausted'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'needs_extreme_nursing'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'has_extreme_nursing'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'is_confused'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'is_dementic'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'residence'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
#
#
# file_name = 'recommended_residence'
# with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
#     slurm_file.write(slurm_config_string.format(
#         file_name,
#         'sequence_classifier',
#         '0 1 2',
#         'roberta',
#         'roberta-large'
#     ))
# os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'sex'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2 3',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'immigrant'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2 3',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'marital_status'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'children'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'closest_relative'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'closest_supporting_relative'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'seeking_help_at_home'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'is_holocaust_survivor'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'is_exhausted'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'needs_extreme_nursing'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'has_extreme_nursing'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'is_confused'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'is_dementic'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'residence'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))


file_name = 'recommended_residence'
with open(os.path.join(slurm_dir, file_name + '.sh'), 'w') as slurm_file:
    slurm_file.write(slurm_config_string.format(
        file_name,
        'pet',
        '0 1 2',
        'roberta',
        'roberta-large'
    ))
os.system(run_string.format(os.path.join(slurm_dir, file_name + '.sh')))
