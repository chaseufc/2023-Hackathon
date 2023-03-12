import openai


def call_api(text):
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    prompt = "for every sentence in the following text, assign that sentence a rating from 0 to 100 for how factual and accurate they are, then once every sentence has a rating, average all of the ratings and output the final average percentage? format the answer as a percentage then explain which parts are false in 20 words using examples of evidence. this is important however, only output a number in percentage form, and 4 sentences that explain the response. \n"

    # long text to be summarized
    out = text

    # generate the summary using the OpenAI API
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt + out,
    temperature=0,
    max_tokens=400,
    n=1,
    stop=None,
    timeout=15,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )["choices"][0]["text"]

    return response


def check_response(text):
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    prompt = "if the following text is free of all derogatory comments and false information then return a 1, if there is inappropriate language return a 0. your output must only be a single digit, 0 or 1. \n"

    # long text to be summarized
    out = text

    # generate the summary using the OpenAI API
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt + out,
    temperature=0,
    max_tokens=400,
    n=1,
    stop=None,
    timeout=15,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )["choices"][0]["text"]

    return response



def main():
    text = input("insert text: \n")
    answer = call_api(text)
    check = check_response(answer)
    if check == 0:
        print('Please ask another question')
    print(check)
    print("\n" * 4)
    print('-' * 150)
    print(answer)
    print('-' * 150)
    print('*** PLEASE NOTE, THE INFORMATION ABOVE IS BASED UPON AN AI MODEL, WHICH MAY HAVE BEEN TRAINED USING INACCURATE DATA, IT IS ONLY A SUGGESTION ***')


main()
