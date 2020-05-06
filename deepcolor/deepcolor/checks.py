CAFFE_IS_INSTALLED = True
try:
    import caffe
except ModuleNotFoundError:
    CAFFE_IS_INSTALLED = False
