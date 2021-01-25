
echo "dublin1"

for IMAGE in "dublin1"
do
	for SCALE in 3 4 5 6 7 8
	do 
		for ROT in -20 -15 -10 -5 -4 -3 -2 -1 0 1 2 3 4 5 10 15 20
		do
			python denoising.py --input_name dublin_1  --ref_name "rotations/${IMAGE}_noisy_${ROT}.png" --harmonization_start_scale $SCALE
		done
	done
done

echo "picasso1"

for IMAGE in "picasso1"
do
	for SCALE in 3 4 5 6 7 8
	do 
		for ROT in -20 -15 -10 -5 -4 -3 -2 -1 0 1 2 3 4 5 10 15 20
		do
			python denoising.py --input_name picasso_1  --ref_name "rotations/${IMAGE}_noisy_${ROT}.png" --harmonization_start_scale $SCALE
		done
	done
done
