#### 1. 声明数据路径(`set_date.sh`)

```
# Set this to where you extracted the downloaded file
export DATA_PATH=

export VOCAB_SOURCE=${DATA_PATH}/vocab.bpe.32000
export VOCAB_TARGET=${DATA_PATH}/vocab.bpe.32000
export TRAIN_SOURCES=${DATA_PATH}/train.tok.clean.bpe.32000.en
export TRAIN_TARGETS=${DATA_PATH}/train.tok.clean.bpe.32000.de
export DEV_SOURCES=${DATA_PATH}/newstest2013.tok.bpe.32000.en
export DEV_TARGETS=${DATA_PATH}/newstest2013.tok.bpe.32000.de

export DEV_TARGETS_REF=${DATA_PATH}/newstest2013.tok.de
export TRAIN_STEPS=1000000
```

#### 1.1 生成较小的数据集

1. 首先执行下列命令会在`~/nmt_data/toy_reverse`目录下生成数据

```
DATA_TYPE=reverse ~/work/gitwork/seq2seq/bin/data/toy.sh
```

2. 设置数据环境变量

```
export VOCAB_SOURCE=${HOME}/nmt_data/toy_reverse/train/vocab.sources.txt
export VOCAB_TARGET=${HOME}/nmt_data/toy_reverse/train/vocab.targets.txt
export TRAIN_SOURCES=${HOME}/nmt_data/toy_reverse/train/sources.txt
export TRAIN_TARGETS=${HOME}/nmt_data/toy_reverse/train/targets.txt
export DEV_SOURCES=${HOME}/nmt_data/toy_reverse/dev/sources.txt
export DEV_TARGETS=${HOME}/nmt_data/toy_reverse/dev/targets.txt

export DEV_TARGETS_REF=${HOME}/nmt_data/toy_reverse/dev/targets.txt
export TRAIN_STEPS=1000
```

#### 2. 定义模型(https://github.com/google/seq2seq/tree/master/example_configs)

```
model: AttentionSeq2Seq
model_params:
  attention.class: seq2seq.decoders.attention.AttentionLayerBahdanau
  attention.params:
    num_units: 256
  bridge.class: seq2seq.models.bridges.ZeroBridge
  embedding.dim: 256
  encoder.class: seq2seq.encoders.BidirectionalRNNEncoder
  encoder.params:
    rnn_cell:
      cell_class: GRUCell
      cell_params:
        num_units: 256
      dropout_input_keep_prob: 0.8
      dropout_output_keep_prob: 1.0
      num_layers: 1
  decoder.class: seq2seq.decoders.AttentionDecoder
  decoder.params:
    rnn_cell:
      cell_class: GRUCell
      cell_params:
        num_units: 256
      dropout_input_keep_prob: 0.8
      dropout_output_keep_prob: 1.0
      num_layers: 2
  optimizer.name: Adam
  optimizer.learning_rate: 0.0001
  source.max_seq_len: 50
  source.reverse: false
  target.max_seq_len: 50
```

#### 3. 




