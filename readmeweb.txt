This is a web api version of the neural style renderer


## AWS Linux initial install ##
* Python 2 is pre-installed, need to get to 3
* for some reason 3.6 is not available so started with 3.7
sudo yum install python37
sudo yum install git
sudo yum install mesa-libGL
# maybe not? sudo -H pip3 install --upgrade pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user

pip install --upgrade --force-reinstall --no-cache-dir tensorflow==1.15.0
pip install scipy
pip install opencv-python
pip install boto3 (aws)
git clone https://github.com/patrickmclean/neural-style-tf.git
wget https://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat (make sure you're in neural style directory)
Test Run: bash stylize_image.sh ./image_input/lion.jpg ./styles/kandinsky.jpg
pip install cherrypy

## Update software ##
Update: git fetch --all; git reset --hard origin/master (or git pull after erasing local copies)
Run: python3 



Install for neural style (old, just for reference):

Steps:
	• If no p3: pip install python36
	•?  Often needed: pip install --upgrade pip
	• If no git: sudo yum install git
		○ If no tensorflow: pip3 install --upgrade --force-reinstall --no-cache-dir tensorflow==1.15.0
	• pip install opencv-python
	• pip install scipy (aws)
	• Install sw: git clone https://github.com/patrickmclean/neural-style-tf.git
	• Update: git fetch --all; get reset --hard origin/master (or git pull after erasing local copies)
	• Download weights:wget https://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat
	• Run: bash stylize_image.sh ./image_input/lion.jpg ./styles/kandinsky.jpg


# not sure if this section is needed. some confusion between conda and pip. 
# am not using virtual environments
This required downgrading to python 3.6 first:
conda install python=3.6.4
Then pip3 install tensorflow1.15 above.


This needs to be run each time the server restarts: why??

Get right Cudnn version
pip install cudnnenv (manages cuda versions)
cudnnenv install v7.6.0-cuda10
LD_LIBRARY_PATH=~/.cudnn/active/cuda/lib64:$LD_LIBRARY_PATH
CPATH=~/.cudnn/active/cuda/include:$CPATH
LIBRARY_PATH=~/.cudnn/active/cuda/lib64:$LIBRARY_PATH
(cuda version nvcc --version)

