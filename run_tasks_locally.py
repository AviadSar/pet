import os

command_string_pet = """python cli.py --method pet --pattern_ids {0} --data_dir "C:\my_documents\datasets\HaddassahRH" --model_type deberta --model_name_or_path "microsoft/deberta-base" --task_name {1} --output_dir "outputs/pet/{1}" --do_train --do_eval --overwrite_output_dir --pet_max_seq_length 256 --sc_max_seq_length 256"""
command_string_ipet = """python cli.py --method ipet --pattern_ids {0} --data_dir "C:\my_documents\datasets\HaddassahRH" --model_type deberta --model_name_or_path "microsoft/deberta-base" --task_name {1} --output_dir "outputs/ipet/{1}" --do_train --do_eval --overwrite_output_dir --pet_max_seq_length 256 --sc_max_seq_length 256"""

# os.system(command_string_pet.format('0 1 2 3', 'sex'))
# os.system(command_string_pet.format('0 1 2 3', 'immigrant'))
# os.system(command_string_pet.format('0 1 2', 'marital_status'))
# os.system(command_string_pet.format('0 1', 'closest_relative'))
# os.system(command_string_pet.format('0 1', 'closest_supporting_relative'))
# os.system(command_string_pet.format('0 1 2', 'seeking_help_at_home'))
# os.system(command_string_pet.format('0 1', 'is_holocaust_survivor'))
# os.system(command_string_pet.format('0 1 2', 'is_exhausted'))
# os.system(command_string_pet.format('0 1', 'needs_extreme_nursing'))
# os.system(command_string_pet.format('0 1', 'has_extreme_nursing'))
# os.system(command_string_pet.format('0 1 2', 'is_confused'))
# os.system(command_string_pet.format('0 1 2', 'is_dementic'))
# os.system(command_string_pet.format('0 1 2', 'residence'))
# os.system(command_string_pet.format('0 1 2', 'recommended_residence'))

# os.system(command_string_ipet.format('0 1 2 3', 'sex'))
# os.system(command_string_ipet.format('0 1 2 3', 'immigrant'))
# os.system(command_string_ipet.format('0 1 2', 'marital_status'))
# os.system(command_string_ipet.format('0 1', 'closest_relative'))
# os.system(command_string_ipet.format('0 1', 'closest_supporting_relative'))
# os.system(command_string_ipet.format('0 1 2', 'seeking_help_at_home'))
os.system(command_string_ipet.format('0 1', 'is_holocaust_survivor'))
# os.system(command_string_ipet.format('0 1 2', 'is_exhausted'))
# os.system(command_string_ipet.format('0 1', 'needs_extreme_nursing'))
# os.system(command_string_ipet.format('0 1', 'has_extreme_nursing'))
# os.system(command_string_ipet.format('0 1 2', 'is_confused'))
# os.system(command_string_ipet.format('0 1 2', 'is_dementic'))
# os.system(command_string_ipet.format('0 1 2', 'residence'))
# os.system(command_string_ipet.format('0 1 2', 'recommended_residence'))
