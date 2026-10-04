import ollama

print('Bot is ready! Type exit to stop')
while True:
  qn=input('You: ')
  if qn.lower()=='exit':
    break
  ans=ollama.chat(model='phi3:mini', messages=[{'role': 'user','content':qn}])
  print("Bot: ",ans['message']['content'])
