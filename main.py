import constants as c
import promptlib as p
import openai
openai.api_key = c.OPENAI_API_KEY


def context_append(context, role, content):
    context.append({"role": role, "content": content})

def init_context():
    context = list()
    context_append(context, "system", p.system_prompt)
    return context

def context_add_prompt(context, prompt_sequence):
    for i in range(len(prompt_sequence) - 1):
        context_append(context, "user", prompt_sequence[i][0])
        context_append(context, "assistant", prompt_sequence[i][1])
    context_append(context, "user", prompt_sequence[-1][0])

def call_api_engine(context, temperature=c.DEFAULT_TEMPERATURE, model=c.DEFAULT_MODEL):
    response = openai.ChatCompletion.create(model=model, messages=context, temperature=temperature)
    return response

def unwrap_reply(response):
    return response['choices'][0]['message']['content']

def main():
    n_correct = 0
    for i in range(100):
        context = init_context()
        sequence = p.make_alphabet_mixed_sequence()
        true_answer = sequence[-1][1]
        context_add_prompt(context, sequence) 
        gpt_answer = unwrap_reply(call_api_engine(context))

        correct = gpt_answer == true_answer
        if correct:
            n_correct += 1

        print("True answer:", true_answer)
        print("GPT answer:", gpt_answer)
        print("Correct?", correct)

    print("Accuracy:", n_correct / 100)

if __name__ == "__main__":
    main()
