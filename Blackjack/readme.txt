pip install snakeviz
python3 -m cProfile -o profile.prof grader.py mdp-values
snakeviz profile.prof
