# function get_frame(vid_name, vid_dir, second)
# 	frames_dir_name = [vid_dir '/' strtok(vid_name, '.')]

#     out_file_name = sprintf('image_%08d.png', second)
#     system(['ffmpeg -ss ' num2str(second) ' -i ' vid_dir '/' vid_name ' -frames:v 1 ' frames_dir_name '/' out_file_name]);
# end

import subprocess
import os
import csv
import scipy
from scipy import io
import numpy

def get_frame(vid_name, vid_dir, frame_num):
	os.system('mkdir ' + frames_dir_name)
	out_file_name = 'image_{:08d}.png'.format(i)
	o = 'ffmpeg -ss ' + str(i) + ' -i ' + vid_dir + '/' + vid_name + ' -frames:v 1 ' + frames_dir_name + '/' + out_file_name
	# print o
	os.system(o)

def download_video(youtubeURL):
	o = 'youtube-dl -o "../../ed-vids/ID-%(id)s.%(ext)s" ' + youtubeURL
	# print o
	os.system(o)

def csv_ids_frames_labels_to_mat(csv_name, matlab_name):
	# reader = csv.reader(open('../vids_to_download/ids_and_frames_training-10-2.csv', 'rb'),delimiter=',')
	reader = csv.reader(open(csv_name, 'rb'),delimimter=',')
	x = list(reader)

	files_list = []
	index_list = []
	label_list = []
	for i in range(5, 28):
	    files_list.append(x[i][0])
	    index_list.append(x[i][2])
	    label_list.append(x[i][4])
	    files_list.append(x[i][0])
	    index_list.append(x[i][5])
	    label_list.append(x[i][7])
	    files_list.append(x[i][0])
	    index_list.append(x[i][8])
	    label_list.append(x[i][10])
	    files_list.append(x[i][0])
	    index_list.append(x[i][11])
	    label_list.append(x[i][13])
	    files_list.append(x[i][0])
	    index_list.append(x[i][14])
	    label_list.append(x[i][16])

	files_list = numpy.array(files_list, dtype=numpy.object)
	index_list = numpy.array(index_list, dtype=numpy.int16)
	label_list = numpy.array(label_list, dtype=numpy.object)

	scipy.io.savemat(matlab_name, mdict={'vid_names': files_list, 'frame_nums': index_list, 'labels': label_list})
	# scipy.io.savemat('../vids_to_download/vid_names_and_frames_and_labels-training-set-10-2.mat', mdict={'vid_names': files_list, 'frame_nums': index_list, 'labels': label_list})

# TODO: write get_frames_from_vid_list_and_frame_list

if __name__=="__main__":
	# max_frame = 257 # get us 256 frames
	# vid_dir = '../../ed-vids'
	# youtubeURL = 'https://www.youtube.com/watch?v=8su-otIh2gA'
	# vid_id = youtubeURL[-11:]

	# download_video(youtubeURL)
	# # missing one step here where you get the name of the video

	# vid_name = 'ID-' + vid_id + '.mp4'

	# frames_dir_name = vid_dir + '/' + vid_name[:-4]

	# for i in range(1, max_frame):
	# 	get_frame(vid_name, vid_dir, i)

	csv_ids_frames_labels_to_mat('../vids_to_download/ids_and_frames_training-10-2.csv', '../vids_to_download/vid_names_and_frames_and_labels-training-set-10-2.mat')

