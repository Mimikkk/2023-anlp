import torch
import torchtext
from torch.utils.data import Dataset
from torchtext.vocab import build_vocab_from_iterator

class ParallelCorpus(Dataset):
    def __init__(self, data, lang_a, lang_b, vocab_a=None, vocab_b=None, data_limit=torch.inf):
        tokenizer_a = torchtext.data.utils.get_tokenizer("spacy", language=lang_a)
        tokenizer_b = torchtext.data.utils.get_tokenizer("spacy", language=lang_b)
        self.texts_a, self.texts_b = [], []
        for i, j in data:
            self.texts_a.append(tokenizer_a(i.strip()))
            self.texts_b.append(tokenizer_b(j.strip()))
            self.texts_a[-1].append("<stop>")
            self.texts_b[-1].append("<stop>")
            self.texts_a[-1].insert(0,"<start>")
            self.texts_b[-1].insert(0,"<start>")
            if len(self.texts_a) >= data_limit :
                break

        if vocab_a is None or vocab_b is None:
            self.vocab_a = build_vocab_from_iterator(self.texts_a, specials=["<pad>", "<unk>", "<start>", "<stop>"], min_freq=2)
            self.vocab_b = build_vocab_from_iterator(self.texts_b, specials=["<pad>", "<unk>", "<start>", "<stop>"], min_freq=2)

            self.vocab_a.set_default_index(1)
            self.vocab_b.set_default_index(1)
        else:
            self.vocab_a, self.vocab_b = vocab_a, vocab_b

        for i,  texts in enumerate(zip(self.texts_a, self.texts_b)):
            self.texts_a[i] = torch.tensor(self.vocab_a(texts[0]), dtype=torch.int64)
            self.texts_b[i] = torch.tensor(self.vocab_b(texts[1]), dtype=torch.int64)
            
    def __len__(self):
        return len(self.texts_a)
    
    def __getitem__(self, item):
        return {'text_a':self.texts_a[item], 'text_b':self.texts_b[item]}
    
    def convert_to_text(self, text_a, text_b):
        return self.vocab_a.lookup_tokens(text_a), self.vocab_b.lookup_tokens(text_b)

def translate(sentence, model, dataset, device, max_len = 50, verbose = True):
    model.eval()
    
    src_tensor = torch.LongTensor(sentence).unsqueeze(1).to(device)
    src_len = torch.LongTensor([len(sentence)])
    
    with torch.no_grad():
        encoder_outputs, hidden = model.encoder(src_tensor, src_len)
        
    trg_indexes = dataset.vocab_b(["<start>"])
    stop_token = dataset.vocab_b(["<stop>"])[0]
    
    for i in range(max_len):

        trg_tensor = torch.LongTensor([trg_indexes[-1]]).to(device)
                
        with torch.no_grad():
            output, hidden = model.decoder(trg_tensor, hidden, encoder_outputs, src_len)
            
        pred_token = output.argmax(1)      
        trg_indexes.append(pred_token)

        if pred_token == stop_token:
            break
            
    trg_tokens = dataset.vocab_b.lookup_tokens(trg_indexes)
    
    if verbose:
        print(f'Żródło = {dataset.vocab_a.lookup_tokens(sentence.numpy())}')
        print(f'Tłumaczenie = {trg_tokens}')

    return trg_tokens

