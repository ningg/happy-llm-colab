# happy-llm-colab （Colab 上，实践 happy-llm）

## 1.Colab 简介

> Colab 上，直接运行 happy-llm 代码，细节参考 [什么是 Colab？](https://colab.research.google.com/notebooks/intro.ipynb#scrollTo=5fCEDCU_qrC0)
> 
> 借助 Colaboratory（简称 `Colab`），您可在浏览器中**编写**和**执行** `Python 代码`，并且：
> 
> * 无需任何配置 
> * 免费使用 GPU
> * 轻松共享
> 
> 无论您是一名学生、数据科学家还是 AI 研究员，Colab 都能够帮助您更轻松地完成工作。观看 [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI)


## 2.目标

**背景**：原始项目[happy-llm](https://github.com/datawhalechina/happy-llm) 不是 `ipynb` 格式文件，无法直接利用 `colab` 运行，效率低。

**焦点**：编写脚本，生成 [happy-llm-colab](https://github.com/ningg/happy-llm-colab) (**happy-llm 的 colab 版本项目**)，用于在 colab 上直接实践 happy-llm 代码。

**备注**：这个项目，会跟 happy-llm 保持`周级别`更新。


![](./happy-llm-colab.png)


## 3.📖 内容导航

> ***Tips***： 直接点击下面`链接`，就会跳转到 `colab` 平台，直接运行 happy-llm 对应代码.

| 章节 | 关键内容 | 状态 |
| --- | --- | --- |
| [前言](https://colab.research.google.com/github/ningg/happy-llm-colab/blob/main/docs/前言.ipynb) | 本项目的缘起、背景及读者建议 | ✅ |
| [第一章 NLP 基础概念](https://colab.research.google.com/github/ningg/happy-llm-colab/blob/main/docs/chapter1/第一章%20NLP基础概念.ipynb) | 什么是 NLP、发展历程、任务分类、文本表示演进 | ✅ |
| [第二章 Transformer 架构](https://colab.research.google.com/github/ningg/happy-llm-colab/blob/main/docs/chapter2/第二章%20Transformer架构.ipynb) | 注意力机制、Encoder-Decoder、手把手搭建 Transformer | ✅ |
| [第三章 预训练语言模型](https://colab.research.google.com/github/ningg/happy-llm-colab/blob/main/docs/chapter3/第三章%20预训练语言模型.ipynb) | Encoder-only、Encoder-Decoder、Decoder-Only 模型对比 | ✅ |
| [第四章 大语言模型](https://colab.research.google.com/github/ningg/happy-llm-colab/blob/main/docs/chapter4/第四章%20大语言模型.ipynb) | LLM 定义、训练策略、涌现能力分析 | ✅ |
| [第五章 动手搭建大模型](https://colab.research.google.com/github/ningg/happy-llm-colab/blob/main/docs/chapter5/第五章%20动手搭建大模型.ipynb) | 实现 LLaMA2、训练 Tokenizer、预训练小型 LLM | ✅ |
| [第六章 大模型训练实践](https://colab.research.google.com/github/ningg/happy-llm-colab/blob/main/docs/chapter6/第六章%20大模型训练流程实践.ipynb) | 预训练、有监督微调、LoRA/QLoRA 高效微调 | 🚧 |
| [第七章 大模型应用](https://colab.research.google.com/github/ningg/happy-llm-colab/blob/main/docs/chapter7/第七章%20大模型应用.ipynb) | 模型评测、RAG 检索增强、Agent 智能体 | ✅ |
| [Extra Chapter LLM Blog](./Extra-Chapter/) | 优秀的大模型 学习笔记/Blog ，欢迎大家来 PR ！| 🚧 |


### Extra Chapter LLM Blog

- [大模型都这么厉害了，微调0.6B的小模型有什么意义？](./Extra-Chapter/why-fine-tune-small-large-language-models/readme.ipynb) @[不要葱姜蒜](https://github.com/KMnO4-zx) 2025-7-11

- [Transformer 整体模块设计解读](./Extra-Chapter/transformer-architecture/readme.ipynb) @[ditingdapeng](https://github.com/ditingdapeng) 2025-7-14

- [文本数据处理详解](./Extra-Chapter/text-data-processing/readme.ipynb) @[蔡鋆捷](https://github.com/xinala-781) 2025-7-14

- [Qwen3-"VL"——超小中文多模态模型的“拼接微调”之路](./Extra-Chapter/vlm-concatenation-finetune/README.ipynb) @[ShaohonChen](https://github.com/ShaohonChen) 2025-7-30

- [S1: Thinking Budget with vLLM](./Extra-Chapter/s1-vllm-thinking-budget/readme.ipynb) @[kmno4-zx](https://github.com/kmno4-zx) 2025-8-03


- [CDDRS: 使用细粒度语义信息指导增强的RAG检索方法](./Extra-Chapter/CDDRS/readme.ipynb) @[Hongru0306](https://github.com/Hongru0306) 2025-8-21


## 附录：happy-llm 生成 happy-llm-colab 的脚本

Automatically Generated Notebooks for Colab

> Tips: 不要手动执行更新文件，直接执行脚本 `./run_all.sh` 即可.


执行脚本之前，需要安装依赖：


```shell
pip install nbformat nbconvert
conda install -c conda-forge pandoc  # 或者用 brew install pandoc

// 改脚本权限
chmod +x run_all.sh
```





