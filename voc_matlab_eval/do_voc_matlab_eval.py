# modified from fast-rcnn/lib/datasets/pascal_voc.py 

import os
import subprocess

#path = '/home/jblin/dev/fast-rcnn/lib/datasets/VOCdevkit-matlab-wrapper'
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'VOCdevkit-matlab-wrapper')
#path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'VOCdevkit2012-matlab-wrapper')

cmd = 'cd {} && '.format(path)
#cmd += '{:s} -nodisplay -nodesktop '.format(datasets.MATLAB)
cmd += 'matlab -nodisplay -nodesktop '
cmd += '-r "dbstop if error; '

#devkit_path = '/home/jblin/dev/fast-rcnn/data/VOCdevkit2007'
devkit_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'VOCdevkit2007')
#devkit_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'VOCdevkit2012')

comp_id = 'comp4-26389'
image_set = 'test'
#output_dir = '/home/jblin/dev/fast-rcnn/output/default/voc_2007_test/yolo'
#output_dir = 'voc_2007_test/yolo'
#output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'voc_2007_test/yolo')
#output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'voc_2012_test/yolo')
#output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'voc_2007_test/alexnet')
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'voc_2007_test/'+comp_id)

rm_results = 0

cmd += 'voc_eval(\'{:s}\',\'{:s}\',\'{:s}\',\'{:s}\',{:d}); quit;"' \
      .format(devkit_path,
              comp_id,
              image_set,
              output_dir,
              int(rm_results))

print('Running:\n{}'.format(cmd))

status = subprocess.call(cmd, shell=True)
