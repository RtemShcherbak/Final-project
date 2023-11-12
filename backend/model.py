# TOKENIZATION
from transformers import AutoTokenizer

#MODEL
from transformers import T5ForConditionalGeneration


def generate_answer(question):
  tokenizer = AutoTokenizer.from_pretrained('cointegrated/rut5-base-multitask')
  source_encoding = tokenizer(
      question['question'],
      question['context'],
      max_length=396,
      padding='max_length',
      truncation=True,
      return_attention_mask=True,
      add_special_tokens=True,
      return_tensors='pt'
  )

  generated_ids = model.generate(
      input_ids=source_encoding['input_ids'],
      attention_mask=source_encoding['attention_mask'],
      num_beams=2,
      max_length=128,
      #repetiton_penalty=1.0,
      early_stopping=True,
      use_cache=True
  )

  preds = [
      tokenizer.decode(generated_id, skip_special_tokens=True, clean_up_tokenizer_spaces=True)
      for generated_id in generated_ids
  ]

  return ''.join(preds)


model =T5ForConditionalGeneration.from_pretrained("finetuned_model")
