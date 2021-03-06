import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from qaPairsRelationClassification.CONVNET.model import CONVNET
import tensorflow as tf
from qaPairsRelationClassification.utils.load_data import load_char_data

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

p, h, y = load_char_data('input/test.csv', data_size=None)

model = CONVNET()
saver = tf.train.Saver()

with tf.Session()as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, '../output/convnet/convnet_7.ckpt')
    loss, acc = sess.run([model.loss, model.acc],
                         feed_dict={model.p: p,
                                    model.h: h,
                                    model.y: y,
                                    model.keep_prob: 1})

    print('loss: ', loss, ' acc:', acc)
