# Astra Fellowship round 2 research exercise


### Test log

|      Task      |       Model        |  n  |  params  | accuracy |
|:--------------:|:------------------:|:---:|:--------:|:--------:|
|    Alphabet    |       gpt-4        | 10  |  p=0.3   |  99/100  |
|     Digits     |       gpt-4        | 10  |  p=0.5   |  89/100  |
|     Digits     |       gpt-4        | 10  |  p=0.75  |  99/100  |
|    Alphabet    | gpt-3.5-turbo-1106 | 10  |  p=0.3   |   7/10   |
|    Alphabet    | gpt-3.5-turbo-1106 | 10  |  p=0.5   |   9/10   |
|    Alphabet    | gpt-3.5-turbo-1106 | 10  |  p=0.5   |  97/100  |
|    Alphabet    | gpt-3.5-turbo-1106 |  5  |  p=0.5   |   9/10   |
|    Alphabet    | gpt-3.5-turbo-1106 |  5  |  p=0.5   |  92/100  |
|     Digits     | gpt-3.5-turbo-1106 |  5  |  p=0.6   |   5/10   |
|     Digits     | gpt-3.5-turbo-1106 |  5  |  p=0.75  |   8/10   |
|     Digits     | gpt-3.5-turbo-1106 |  5  |  p=0.8   |   8/10   |
|     Digits     | gpt-3.5-turbo-1106 | 10  |  p=0.8   |  91/100  |
| Alphabet-words | gpt-3.5-turbo-1106 |  5  | p=0.0006 |   5/10   |
| Alphabet-words | gpt-3.5-turbo-1106 | 10  | p=0.0010 |   8/10   |
| Alphabet-words | gpt-3.5-turbo-1106 | 10  | p=0.0010 |  97/100  |
| Alphabet-words | gpt-3.5-turbo-1106 |  5  | p=0.0010 |  86/100  |
| Alphabet-words | gpt-3.5-turbo-1106 |  7  | p=0.0010 |  84/100  |
| Alphabet-words | gpt-3.5-turbo-1106 | 10  | p=0.0010 |  91/100  |