import os
import glob
import pandas as pd

def unique_list(list_label):
	u_list = []

	for i in list_label:
		if i not in u_list:
			u_list.append(i)
	return u_list

def count_images(root, folder):
	imgs = glob.glob(os.path.join(root, folder) + '/*.jpg')
	return len(imgs)

def nimages_label(root, file):
	# Reading csv file of GENE and LABEL
	listofelements = pd.read_csv(file, header=0)

	# cleaning multilabels
	multi_label_indices = [i for i, label in enumerate(listofelements['label']) if ';' in label]
	for i in multi_label_indices:
			listofelements = listofelements.drop([i])
	listofelements = listofelements.reset_index()

	# u_l = unique_list(listofelements['label'])

	# setting a unique labels
	# it is possible to use the built-in function "set ()" or the method I have defined above "unique_list"
	uniq_label = set(listofelements['label'])
	# creating an empty dictionary of labels as a key and number of images of different Gene as a value
	images_dict = dict()
	for ul in uniq_label:
		# initializing labels as a key
		images_dict[ul] = []
		# adding images as a list to each key(label)
		for i, j in enumerate(listofelements['label']):
			if int(listofelements['label'][i]) == int(ul):
				# count_images func returns length of each folder that contains images
				images_dict[ul].append(count_images(root, listofelements['Gene'][i]))
	# creating an empty dict of unique labels which contains labels and sum of the corresponding images.
	labels_imgs = dict()
	for i in images_dict:
		labels_imgs[i] = sum(images_dict[i])

	return labels_imgs

# driver code
data_distr = nimages_label(root='/home/lhc/2019/cvpr2020/hpa2020/hpa/', file='/home/lhc/2019/cvpr2020/hpa2020/enhanced.csv')
print(data_distr)

def nimages_label_train(root, file):
	# Reading csv file of GENE and LABEL
	listofelements = pd.read_csv(file, header=0)

	# cleaning multilabels
	multi_label_indices = [i for i, label in enumerate(listofelements['label']) if ';' in label]
	for i in multi_label_indices:
			listofelements = listofelements.drop([i])
	listofelements = listofelements.reset_index()

	# u_l = unique_list(listofelements['label'])

	# setting a unique labels
	# it is possible to use the built-in function "set ()" or the method I have defined above "unique_list"
	uniq_label = set(listofelements['label'])
	# creating an empty dictionary of labels as a key and number of images of different Gene as a value
	images_dict = dict()
	for ul in uniq_label:
		# initializing labels as a key
		images_dict[ul] = []
		# adding images as a list to each key(label)
		for i, j in enumerate(listofelements['label']):
			if int(listofelements['label'][i]) == int(ul):
				# count_images func returns length of each folder that contains images
				images_dict[ul].append(count_images(root, listofelements['Gene'][i]))
	# creating an empty dict of unique labels which contains labels and sum of the corresponding images.
	labels_imgs_train = dict()
	for i in images_dict:
		labels_imgs_train[i] = round(sum(images_dict[i])*0.8)
		
	return labels_imgs_train

data_distr_train = nimages_label_train(root='/home/lhc/2019/cvpr2020/hpa2020/hpa/', file='/home/lhc/2019/cvpr2020/hpa2020/enhanced.csv')
print(data_distr_train)

def nimages_label_test(root, file):
	# Reading csv file of GENE and LABEL
	listofelements = pd.read_csv(file, header=0)

	# cleaning multilabels
	multi_label_indices = [i for i, label in enumerate(listofelements['label']) if ';' in label]
	for i in multi_label_indices:
			listofelements = listofelements.drop([i])
	listofelements = listofelements.reset_index()

	# u_l = unique_list(listofelements['label'])

	# setting a unique labels
	# it is possible to use the built-in function "set ()" or the method I have defined above "unique_list"
	uniq_label = set(listofelements['label'])
	# creating an empty dictionary of labels as a key and number of images of different Gene as a value
	images_dict = dict()
	for ul in uniq_label:
		# initializing labels as a key
		images_dict[ul] = []
		# adding images as a list to each key(label)
		for i, j in enumerate(listofelements['label']):
			if int(listofelements['label'][i]) == int(ul):
				# count_images func returns length of each folder that contains images
				images_dict[ul].append(count_images(root, listofelements['Gene'][i]))
	# creating an empty dict of unique labels which contains labels and sum of the corresponding images.
	labels_imgs_test = dict()
	for i in images_dict:
		labels_imgs_test[i] = round(sum(images_dict[i])*0.2)
		
	return labels_imgs_test

data_distr_test = nimages_label_test(root='/home/lhc/2019/cvpr2020/hpa2020/hpa/', file='/home/lhc/2019/cvpr2020/hpa2020/enhanced.csv')
print(data_distr_test)
