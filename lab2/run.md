cat ratings.txt features.txt | python mapper.py | sort | python reducer1.py | sort | python reducer2.py
