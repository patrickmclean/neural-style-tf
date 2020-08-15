# Set right version for Cuda
cudnnenv install v7.6.0-cuda10
LD_LIBRARY_PATH=~/.cudnn/active/cuda/lib64:$LD_LIBRARY_PATH
CPATH=~/.cudnn/active/cuda/include:$CPATH
LIBRARY_PATH=~/.cudnn/active/cuda/lib64:$LIBRARY_PATH
