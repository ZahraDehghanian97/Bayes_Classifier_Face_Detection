import math
import os
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt


def load_images(directory, flag):
    one_dim = []
    for filename in os.listdir(directory):
        path = directory + "/" + filename
        im = mpimg.imread(path)
        for row in im:
            for w in row:
                if flag:
                    img_gray = round(w[0] * 299. / 1000 + w[1] * 587. / 1000 + w[2] * 114. / 1000, 3)
                    one_dim.append(img_gray)
                else:
                    one_dim.append(w[0])

    return one_dim


def seprate(data, label):
    face = []
    non_face = []
    for i in range(len(label)):
        if label[i] == 0:
            face.append(data[i])
        else:
            non_face.append(data[i])
    return face, non_face


def a():
    global face, non_face
    total = len(face) + len(non_face)
    prior_face = len(face) / total
    prior_non_face = len(non_face) / total
    return prior_face, prior_non_face


def b():
    global face, non_face
    means = []
    varianses = []
    means.append(np.mean(face))
    means.append(np.mean(non_face))
    varianses.append(np.var(face))
    varianses.append(np.var(non_face))
    return means, varianses


def Gaussian_distribution(mean, variance, x):
    ans = 1 / math.sqrt(2 * math.pi * variance) * math.exp(-((x - mean) ** 2) / (2 * variance))
    return ans


def classifier(means, varianses, test_data, threshold):
    p = []
    counter = 0
    for data in test_data:
        # counter+=1
        s1 = Gaussian_distribution(means[0], varianses[0], data)
        s2 = Gaussian_distribution(means[1], varianses[1], data)
        s = s1 / s2
        # print('pixel #'+str(counter)+' : ratio gaussian face/non-face : '+str(s)+' threshold : '+str(threshold))
        if s > threshold:
            p.append(0)
        else:
            p.append(1)
    return p


def show_result(predicted_label):
    test_data = []
    directory = "D:/univesity/foqelisans/pattern_recognition/SPR_HW2/code/Q7/Dataset/Test/Masks"
    for filename in os.listdir(directory):
        path = directory + "/" + filename
        im = mpimg.imread(path)
        test_data.append(im)
    result = []
    counter = 0
    for data in test_data:
        pic = []
        for r in data:
            row = []
            for c in r:
                row.append(
                    [predicted_label[counter] * 255, predicted_label[counter] * 255, predicted_label[counter] * 255])
                counter += 1
            pic.append(row)
        result.append(pic)
    counter = 1
    fig = plt.figure()
    for img in result:
        fig.add_subplot(1, 3, counter)
        counter += 1
        plt.imshow(img, cmap='gray')
    plt.show()


def c(prior_face, prior_non_face, means, variances):
    global face, non_face
    threshold = prior_non_face / prior_face
    test_data = load_images("D:/univesity/foqelisans/pattern_recognition/SPR_HW2/code/Q7/Dataset/Test/Images", True)
    predicted_label = classifier(means, variances, test_data, threshold)
    show_result(predicted_label)
    test_label = load_images("D:/univesity/foqelisans/pattern_recognition/SPR_HW2/code/Q7/Dataset/Test/Masks", False)
    true = 0
    for i in range(len(test_label)):
        if test_label[i] == predicted_label[i]:
            true += 1
    print('accuracy = ' + str(true / len(test_label)))
    return test_label, predicted_label


def d(true_label, predicted_label):
    confusion


train_data = load_images("D:/univesity/foqelisans/pattern_recognition/SPR_HW2/code/Q7/Dataset/Train/Images", True)
train_class = load_images("D:/univesity/foqelisans/pattern_recognition/SPR_HW2/code/Q7/Dataset/Train/Masks", False)
face, non_face = seprate(train_data, train_class)

prior_face, prior_non_face = a()
print("prior face class : " + str(prior_face))
print("prior non-face class : " + str(prior_non_face))

means, varianses = b()
print("\nmean face class : " + str(means[0]) + " \nvar face class : " + str(varianses[0]))
print("---------------\nmean non-face class : " + str(means[1]) + " \nvar non-face class : " + str(varianses[1]))

true_label, predicted_label = c(prior_face, prior_non_face, means, varianses)

d(true_label, predicted_label)
