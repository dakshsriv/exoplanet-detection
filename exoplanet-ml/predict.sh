export KEPLER_DATA_DIR=${HOME}/Projects/cshallue/exoplanet-ml/data
export MODEL_DIR=${HOME}/Projects/cshallue/exoplanet-ml/astronet/model



wget -nH --cut-dirs=6 -r -l0 -c -N -np -erobots=off -R 'index*' -A _llc.fits \
  -P ${KEPLER_DATA_DIR}/0114/011442793 \
  http://archive.stsci.edu/pub/kepler/lightcurves/0114/011442793/



#python3 astronet/predict.py \
#  --model=AstroCNNModel \
#  --config_name=local_global \
#  --model_dir=${MODEL_DIR} \
#  --kepler_data_dir=${KEPLER_DATA_DIR} \
#  --kepler_id=11442793 \
#  --period=14.44912 \
#  --t0=2.2 \
#  --duration=0.11267 \
#  --output_image_file="${HOME}/astronet/kepler-90i.png"

bazel-bin/astronet/predict   --model=AstroCNNModel   --config_name=local_global   --model_dir=/home/daksh/Projects/cshallue/exoplanet-ml/astronet/model   --kepler_data_dir=/home/daksh/Projects/cshallue/exoplanet-ml/data   --kepler_id=11442793   --period=14.44912   --t0=2.2   --duration=0.11267   --star_radius=1.2 --real_radius=1.32

