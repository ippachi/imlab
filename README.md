## ディレクトリ構造

```
project_root
├── data
│   ├── model
│   ├── neg
│   └── pos
├── input
│   └── video
└── src
    ├── cascade.py
    ├── neg.txt
    ├── positive.vec
    └── pos.txt
```

こんな感じにしたらコマンドがいい感じにしてくれる



## bin以下のコマンド使用法

### cascasde
`bin/cascade [-f feature type] [-w width] [-h height] [-m minHitRate] [-s numStages] human_detect`

### create\_sample
`bin/create_sample human_detect width height`

