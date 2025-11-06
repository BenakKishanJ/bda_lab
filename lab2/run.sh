cat user_item_ratings.txt item_feature.txt | python mapper.py | sort | python reducer1.py | sort | python reducer2.py
