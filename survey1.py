import gradio as gr


def show_answers(q1, q2, q3, q4, q5):
    result = "提交结果：\n"
    result += f"1. {q1}\n2. {q2}\n3. {q3}\n4. {q4}\n"
    result += f"5. {', '.join(q5) if q5 else '未选择'}"
    return result


with gr.Blocks(title="计算机组成原理调查问卷", theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🖥️ 计算机组成原理课程学习情况调查及辅导建议")

    # 问题1
    with gr.Row():
        q1 = gr.Radio(
            label="1. 在进入本课程之前，你是否学过数字电路、模拟电路等先修课程？",
            choices=["全部学过且掌握良好",
                     "学过部分，有一定基础",
                     "仅听说过，不太了解内容",
                     "完全没学过"],
            interactive=True
        )

    # 问题2
    with gr.Row():
        q2 = gr.Radio(
            label="2. 你对计算机硬件有浓厚的兴趣吗？",
            choices=["非常感兴趣，经常主动了解相关知识",
                     "比较感兴趣，愿意花时间学习",
                     "兴趣一般，因专业要求才学习",
                     "不感兴趣，觉得枯燥难懂"],
            interactive=True
        )

    # 问题3
    with gr.Row():
        q3 = gr.Radio(
            label="3. 你是否了解计算机的基本组成部分（如 CPU、内存、硬盘等）及其功能？",
            choices=["非常熟悉，能详细阐述原理",
                     "知道各部件名称和基本功能",
                     "仅听说过部分部件名称",
                     "完全不了解"],
            interactive=True
        )

    # 问题4
    with gr.Row():
        q4 = gr.Radio(
            label="4. 你有没有自学过与计算机组成原理相关的课外知识？",
            choices=["经常自学，阅读大量资料",
                     "偶尔自学，了解一些拓展内容",
                     "想过自学，但没付诸行动",
                     "从未有过自学想法"],
            interactive=True
        )

    # 问题5（多选）
    with gr.Row():
        q5 = gr.CheckboxGroup(
            label="5. 你希望在本课程结束后，自己能达到什么程度？",
            choices=["熟练掌握计算机组成原理的核心知识，能应对考试",
                     "具备分析计算机硬件系统问题的能力",
                     "能够设计简单的计算机硬件组件",
                     "仅为完成学业要求，拿到学分"],
            interactive=True
        )

    submit_btn = gr.Button("📩 提交问卷", variant="primary")
    output = gr.Textbox(label="📋 问卷结果", lines=6)

    submit_btn.click(
        fn=show_answers,
        inputs=[q1, q2, q3, q4, q5],
        outputs=output
    )

demo.launch(share=False)