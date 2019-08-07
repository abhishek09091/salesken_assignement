from flask import Flask, request
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.metrics.pairwise import  cosine_similarity

app = Flask(__name__)


def embed_useT(module):
    with tf.Graph().as_default():
        sentences = tf.placeholder(tf.string)
        embed = hub.Module(module)
        embeddings = embed(sentences)
        session = tf.train.MonitoredSession()
    return lambda x: session.run(embeddings, {sentences: x})


@app.route('/calculate_vector', methods=['POST'])
def calculate_matrix():
    messages = []
    if request.method == 'POST':

        if request.form['strings'] == "":
            return "Please provide strings as a body Example key = strings and value = 'we dont " \
                   "deliver to baner region in pune','we will get you the best possible rate' "
        messages = [x.strip() for x in request.form['strings'].split(',')]
        print(messages)
    embed_fn = embed_useT("https://tfhub.dev/google/universal-sentence-encoder-large/3")
    rows = len(messages)
    result_matrix = []
    for i in range(rows):
        matrix = []
        for j in range(rows):
            temp_1 = embed_fn([messages[i]])
            temp_2 = embed_fn([messages[j]])
            result = cosine_similarity(temp_1, temp_2)
            replace_brackets = result.__str__().replace("[", "")
            replace_brackets = replace_brackets.replace("]", "")
            matrix.append(replace_brackets)
            print("matrix", matrix)
        print()
        result_matrix.append(matrix)

    return result_matrix.__str__()


if __name__ == '__main__':
    app.run(debug=True)