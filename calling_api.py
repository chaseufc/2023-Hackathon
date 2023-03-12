import openai
from Scraping_url import scrape


def call_api(text):
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    prompt = "for every sentence in the following text, assign that sentence a rating from 0 to 100 for how factual and accurate they are, then once every sentence has a rating, average all of the ratings and output the final average percentage? format the answer as a percentage then explain which parts are false in 20 words using examples of evidence. this is important however, only output a number in percentage form, and 4 sentences that explain \n"

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

    print("\n" * 4)
    print('-' * 150)
    print(answer)
    print('-' * 150)
    print('*** PLEASE NOTE, THE INFORMATION ABOVE IS BASED UPON AN AI MODEL, WHICH MAY HAVE BEEN TRAINED USING INACCURATE DATA, IT IS ONLY A SUGGESTION ***')


main()
