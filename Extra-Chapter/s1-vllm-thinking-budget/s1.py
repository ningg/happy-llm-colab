from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
import time

def build_input(prompt, tokenizer):
    messages = [
        {"role": "system", "content": "Please reason step by step, and put your final answer within \\boxed{{}}."},
        {"role": "user", "content": prompt}
    ]
    input_text = tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True,
        enable_thinking=True
    )
    return input_text

def count_thinking_token(outputs, tokenizer):
    total_token = outputs[0].prompt + outputs[0].outputs[0].text
    thinking_token = total_token.split("<think>\n")[-1]
    thinking_token_id = tokenizer(thinking_token)["input_ids"]
    return total_token, len(thinking_token_id)

def count_token(string, tokenizer):
    return len(tokenizer(string)["input_ids"])


def run_thinking_budget_sample(llm_model, tokenizer, user_input, thinking_budget):
    input_text = build_input(user_input, tokenizer)
    input_token_count = count_token(input_text, tokenizer)

    iteration_count= 0
    max_token = input_token_count + thinking_budget

    sampling_params = SamplingParams(
        temperature=0.7,
        max_tokens=4096,
        skip_special_tokens=False
    )

    think_token_count = 0

    while True:

        wait_sampling_params = SamplingParams(
            temperature=0.7,
            max_tokens=thinking_budget - think_token_count,
            stop='</think>',
            skip_special_tokens=False
        )

        outputs = llm_model.generate(
            input_text,
            wait_sampling_params
        )
        total_token, think_token_count = count_thinking_token(outputs, tokenizer)

        print(f'第{iteration_count}次迭代，思考token数：{think_token_count}')

        if think_token_count > thinking_budget:
            break
        input_text = total_token + "\nWait!\n"

        # \nWait a moment. Was there any loophole in my thought just now?!\n
        # \nWait!\n

        iteration_count += 1

    final_outputs = llm_model.generate(
        outputs[0].prompt + outputs[0].outputs[0].text + "\n</think>\n",
        sampling_params
    )   
    
    total_content = final_outputs[0].prompt + final_outputs[0].outputs[0].text
    thinking_content = total_content.split("<think>")[-1].split("</think>")[0]

    print(total_content)

    print(f"迭代次数：{iteration_count}, 输入token数：{input_token_count}, 思考token数：{count_token(thinking_content, tokenizer)}, 总token数：{count_token(total_content, tokenizer)}")

    # 保存输出到文件
    with open(f"output_{int(time.time())}.txt", "w") as f:
        f.write(total_content)
        f.write(f"\n迭代次数：{iteration_count}, 输入token数：{input_token_count}, 思考token数：{count_token(thinking_content, tokenizer)}, 总token数：{count_token(total_content, tokenizer)}")


def run_sample(llm_model, tokenizer, user_input):
    input_text = build_input(user_input, tokenizer)
    input_token_count = count_token(input_text, tokenizer)

    sampling_params = SamplingParams(
        temperature=0.7,
        max_tokens=32768,
        skip_special_tokens=False
    )

    final_outputs = llm_model.generate(
        input_text,
        sampling_params
    )

    total_content = final_outputs[0].prompt + final_outputs[0].outputs[0].text
    thinking_content = total_content.split("<think>")[-1].split("</think>")[0]
    print(total_content)

    print(f"输入token数：{input_token_count}, 思考token数：{count_token(thinking_content, tokenizer)}, 总token数：{count_token(total_content, tokenizer)}")


if __name__ == "__main__":
    model_path = "/model/ModelScope/Qwen/Qwen3-14B"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    llm = LLM(
        model=model_path, 
        gpu_memory_utilization=0.9,
        trust_remote_code=True
    )

    print("=================================== 思考预算采样 ===================================")
    run_thinking_budget_sample(
        llm_model=llm,
        tokenizer=tokenizer,
        user_input="There are exactly three positive real numbers $ k $ such that the function\n$ f(x) = \\frac{(x - 18)(x - 72)(x - 98)(x - k)}{x} $\ndefined over the positive real numbers achieves its minimum value at exactly two positive real numbers $ x $. Find the sum of these three values of $ k $.",
        thinking_budget=32768
    )

    # print("=================================== 无思考预算采样 ===================================")
    # run_sample(
    #     llm_model=llm,
    #     tokenizer=tokenizer,
    #     user_input="There are exactly three positive real numbers $ k $ such that the function\n$ f(x) = \\frac{(x - 18)(x - 72)(x - 98)(x - k)}{x} $\ndefined over the positive real numbers achieves its minimum value at exactly two positive real numbers $ x $. Find the sum of these three values of $ k $."
    # )
