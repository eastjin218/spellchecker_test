import os, glob

#with open('./data/spell.shuf.tsv','r',encoding='utf-8') as f:
#    tmp = f.readlines()
#num = len(tmp)
## train, valid, test
#os.system(f'head -n {round(num*.88)} ./data/spell.shuf.tsv > ./data/spell.shuf.train.tsv')
#os.system(f'tail -n {round(num*.06)} ./data/spell.shuf.tsv | head -n {round(num*.06)} > ./data/spell.shuf.valid.tsv') 
#os.system(f'tail -n {round(num*.06)} ./data/spell.shuf.tsv  > ./data/spell.shuf.test.tsv') 

## err, co
os.system('cut -f1 ./data/spell.shuf.train.tsv > ./data/spell.shuf.train.err')
os.system('cut -f2 ./data/spell.shuf.train.tsv > ./data/spell.shuf.train.co')
os.system('cut -f1 ./data/spell.shuf.valid.tsv > ./data/spell.shuf.valid.err')
os.system('cut -f2 ./data/spell.shuf.valid.tsv > ./data/spell.shuf.valid.co')
os.system('cut -f1 ./data/spell.shuf.test.tsv > ./data/spell.shuf.test.err')
os.system('cut -f2 ./data/spell.shuf.test.tsv > ./data/spell.shuf.test.co')

## set space remove
os.system('python tmp.py')

## mecab 
os.system('cat ./data/spell.shuf.train.err | mecab -O wakati -b 99999 |python post_token.py ./data/spell.shuf.train.err > data/spell.shuf.train.tok.err')
os.system('cat ./data/spell.shuf.train.co | mecab -O wakati -b 99999 |python post_token.py ./data/spell.shuf.train.co > data/spell.shuf.train.tok.co')
os.system('cat ./data/spell.shuf.test.err | mecab -O wakati -b 99999 |python post_token.py ./data/spell.shuf.test.err > data/spell.shuf.test.tok.err')
os.system('cat ./data/spell.shuf.test.co | mecab -O wakati -b 99999 |python post_token.py ./data/spell.shuf.test.co > data/spell.shuf.test.tok.co')
os.system('cat ./data/spell.shuf.valid.err | mecab -O wakati -b 99999 |python post_token.py ./data/spell.shuf.valid.err > data/spell.shuf.valid.tok.err')
os.system('cat ./data/spell.shuf.valid.co | mecab -O wakati -b 99999 |python post_token.py ./data/spell.shuf.valid.co > data/spell.shuf.valid.tok.co')

## bp model
#os.system('python ./subword-nmt/learn_bpe.py --input data/spell.shuf.train.tok.err --output data/bpe.err.model --symbols 50000')
#os.system('python ./subword-nmt/learn_bpe.py --input data/spell.shuf.train.tok.co --output data/bpe.co.model --symbols 50000')

# apply bpe
os.system('python ./subword-nmt/apply_bpe.py --input data/spell.shuf.train.tok.err -c ori_data/bpe.err.model --output data/spell.shuf.train.tok.bpe.err')
os.system('python ./subword-nmt/apply_bpe.py --input data/spell.shuf.test.tok.err -c ori_data/bpe.err.model --output data/spell.shuf.test.tok.bpe.err')
os.system('python ./subword-nmt/apply_bpe.py --input data/spell.shuf.valid.tok.err -c ori_data/bpe.err.model --output data/spell.shuf.valid.tok.bpe.err')
os.system('python ./subword-nmt/apply_bpe.py --input data/spell.shuf.train.tok.co -c ori_data/bpe.co.model --output data/spell.shuf.train.tok.bpe.co')
os.system('python ./subword-nmt/apply_bpe.py --input data/spell.shuf.test.tok.co -c ori_data/bpe.co.model --output data/spell.shuf.test.tok.bpe.co')
os.system('python ./subword-nmt/apply_bpe.py --input data/spell.shuf.valid.tok.co -c ori_data/bpe.co.model --output data/spell.shuf.valid.tok.bpe.co')
 
