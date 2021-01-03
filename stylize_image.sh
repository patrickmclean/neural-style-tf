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
device='/cpu:0'



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

if [ -z "$3"]; then
    output_dir='results'
    output_filename=$(date +%m-%d-%Y-%H-%M)
fi

echo "Rendering stylized image ${output_filename}. This may take a while..."
python neural_style.py \
--content_img "${content_filename}" \
--content_img_dir "${content_dir}" \
--style_imgs "${style_filename}" \
--style_imgs_dir "${style_dir}" \
--img_output_dir "${output_dir}" \
--img_name "${output_filename}" \
--device "${device}" \
--max_size 1024 \
--verbose;

# --max_size 1024
# --original_colors
# --content_weight: Weight for the content loss function. Default: 5e0
#--style_weight: Weight for the style loss function. Default: 1e4
# --content_layers: Space-separated VGG-19 layer names used for the content image. Default: conv4_2 (try 3_2, or 2_2)