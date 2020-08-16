set -e
# Get a carriage return into `cr`
cr=`echo $'\n.'`
cr=${cr%.}

if [ "$#" -le 1 ]; then
   echo "Usage: bash stylize_image.sh <path_to_content_image> <path_to_style_image>"
   exit 1
fi

if [ -z "$var" ]
then
      echo "\$var is empty"
else
      echo "\$var is NOT empty"
fi



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

echo "Rendering stylized image ${output_dir} ${output_filename}. This may take a while..."