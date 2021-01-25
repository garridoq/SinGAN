echo "picasso1"

for IMAGE in "picasso1" "picasso1_f" "picasso2" "starry_night2"
do
	for SCALE in 3 4 5 6 7 8
	do 
		python denoising.py --input_name picasso_1 --ref_name "${IMAGE}_noisy.png" --harmonization_start_scale $SCALE
	done
done
