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
    n_total = c.N_TEST_CALLS
    for i in range(n_total):
        context = init_context()
        sequence = p.make_alphabet_words_mixed_sequence()
        str_to_classify = sequence[-1][0]
        true_label = sequence[-1][1]
        context_add_prompt(context, sequence) 
        gpt_label = unwrap_reply(call_api_engine(context))

        correct = gpt_label == true_label
        print("Input:", str_to_classify)
        print("True label:", true_label)
        print("GPT label:", gpt_label)
        print("Correct?", correct, "\n")
        if correct:
            n_correct += 1
            context_append(context, "assistant", gpt_label)
            context_append(context, "user", p.correct_prompt)
            gpt_explanation = unwrap_reply(call_api_engine(context))
            print("GPT explains:", gpt_explanation, "\n")

    print("Accuracy:", n_correct / n_total)

if __name__ == "__main__":
    main()
