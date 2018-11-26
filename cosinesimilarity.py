import math
from collections import Counter



def build_sentence_vector(sentence1, sentence2):
    iterable1 = sentence1.split()
    iterable2 = sentence2.split()


    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    all_items = set(counter1.keys()).union(set(counter2.keys()))

    # print("Counter 1 : ", counter1)
    # print("Counter 2: ", counter2)
    # print("All items : ", all_items)


    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2


def cosineSimilarity(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)


def start() : 
    
    sentence = "The man is from america is going"
    sentence_ = "boy is going to give the  visa"

    vector1, vector2 = build_sentence_vector(sentence, sentence_)
    similarity = cosineSimilarity(vector1, vector2)

    print("Vectors : ", vector1, vector2)
    print("Similarity : ", similarity)

    angle_in_radians = math.acos(similarity)

    print("Angle in radian : ", angle_in_radians)

    degree =  math.degrees(angle_in_radians)
    print("Degree : ", degree)


start()