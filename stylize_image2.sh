set -e
# Get a carriage return into `cr`
cr=`echo $'\n.'`
cr=${cr%.}

if [ "$#" -le 1 ]; then
   echo "Usage: bash stylize_image.sh <path_to_content_image> <path_to_style_image>"
   exit 1
fi

#echo ""
#read -p "Did you install the required dependencies? [y/n] $cr > " dependencies

#if [ "$dependencies" != "y" ]; then
#  echo "Error: Requires dependencies: tensorflow, opencv2 (python), scipy"
#  exit 1;
#fi

#echo ""
#read -p "Do you have a CUDA enabled GPU? [y/n] $cr > " cuda

#if [ "$cuda" != "y" ]; then
#  device='/cpu:0'
#else
#  device='/gpu:0'
#fi
device='/gpu:0'

# Parse arguments
content_image="$1"
content_dir=$(dirname "$content_image")
content_filename=$(basename "$content_image")

style_image="$2"
style_dir=$(dirname "$style_image" )
style_filename=$(basename "$style_image")

output_image="$3"
output_dir=$(dirname "$output_image" )
output_filename=$(basename "$output_image")

# Defaults
echo "Rendering stylized image. This may take a while..."
python neural_style.py \
--content_img "${content_filename}" \
--content_img_dir "${content_dir}" \
--style_imgs "${style_filename}" \
--style_imgs_dir "${style_dir}" \
--img_output_dir: "${output_dir}" \
--img_name: "r1.jpg" \
--device "${device}" \
--verbose;

# Color
echo "Rendering stylized image. This may take a while..."
python neural_style.py \
--content_img "${content_filename}" \
--content_img_dir "${content_dir}" \
--style_imgs "${style_filename}" \
--style_imgs_dir "${style_dir}" \
--img_output_dir: "${output_dir}" \
--original_colors \
--img_name: "r2.jpg" \
--device "${device}" \
--verbose;

# Lower convolution layer
echo "Rendering stylized image. This may take a while..."
python neural_style.py \
--content_img "${content_filename}" \
--content_img_dir "${content_dir}" \
--style_imgs "${style_filename}" \
--style_imgs_dir "${style_dir}" \
--img_output_dir: "${output_dir}" \
--content_layers: "conv1_2" \
--img_name: "r3.jpg" \
--device "${device}" \
--verbose;

# More weight on source
echo "Rendering stylized image. This may take a while..."
python neural_style.py \
--content_img "${content_filename}" \
--content_img_dir "${content_dir}" \
--style_imgs "${style_filename}" \
--style_imgs_dir "${style_dir}" \
--img_output_dir: "${output_dir}" \
--content_weight: "9e0" \
--img_name: "r4.jpg" \
--device "${device}" \
--verbose;

# More weight on style
echo "Rendering stylized image. This may take a while..."
python neural_style.py \
--content_img "${content_filename}" \
--content_img_dir "${content_dir}" \
--style_imgs "${style_filename}" \
--style_imgs_dir "${style_dir}" \
--img_output_dir: "${output_dir}" \
--style_weight: "5e4" \
--img_name: "r5.jpg" \
--device "${device}" \
--verbose;

# Different source
echo "Rendering stylized image. This may take a while..."
python neural_style.py \
--content_img "${content_filename}" \
--content_img_dir "${content_dir}" \
--style_imgs "rembrandtportrait.jpg" \
--style_imgs_dir "${style_dir}" \
--img_output_dir: "${output_dir}" \
--img_name: "r6.jpg" \
--device "${device}" \
--verbose;

# --max_size 1024
# --original_colors
# --content_weight: Weight for the content loss function. Default: 5e0
#--style_weight: Weight for the style loss function. Default: 1e4
# --content_layers: Space-separated VGG-19 layer names used for the content image. Default: conv4_2 (try 3_2, or 2_2)