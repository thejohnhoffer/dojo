import os
import shutil

from nipy.core.api import Image, AffineTransform

from nipy.io.api import save_image

import tifffile as tif

import numpy as np

def create(rootdir):

  out = None
  prev = None

  out_is_there = False

  dirs = sorted(os.listdir(rootdir))

  for d in dirs:

    files = os.listdir(os.path.join(rootdir,d))

    for f in files:
      input_image = tif.imread(os.path.join(rootdir,d,f))
      # print input_image
      # print type(input_image)
      # print 'ccc',input_image.flatten()
      if out_is_there:
        #out = np.concatenate([out, input_image.flatten()])
        out = np.dstack([out, input_image])
      else:
        # out = input_image.flatten()
        out = input_image
        out_is_there = True

  length = out.shape[0]
  print 'aaa'
  print out
  # out = out.reshape((512, 512, length/512/512))
  print out
  cmap = AffineTransform('kji','zxy', np.eye(4))
  img = Image(out, cmap)
  save_image(img, '/tmp/out.nii.gz')

create('/home/d/TMP/MOJO/ac3x75/mojo/images/tiles/w=00000001')

