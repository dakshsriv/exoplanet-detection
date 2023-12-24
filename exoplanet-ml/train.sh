# Directory to save model checkpoints into.
MODEL_DIR="${HOME}/Projects/exoplanet-detection/exoplanet-ml/astronet/model"
TFRECORD_DIR="${HOME}/Projects/exoplanet-detection/exoplanet-ml/data"

# Run the training script.
bazel-bin/astronet/train \
  --model=AstroCNNModel \
  --config_name=local_global \
  --train_files=${TFRECORD_DIR}/train* \
  --eval_files=${TFRECORD_DIR}/val* \
  --model_dir=${MODEL_DIR}
