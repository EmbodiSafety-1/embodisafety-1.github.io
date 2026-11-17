"""Bilingual overview of the benchmark's purpose and decision requirements."""

PARAGRAPHS = [
    (
        "Recognising a dangerous scene is only part of safe robot behaviour: an agent must also decide whether and how to act on a user's request. "
        "We introduce {strong}EmbodiSafety{/strong} to evaluate this decision process, from interpreting visual evidence to specifying an appropriate next step. "
        "The task requires a response that accounts for the user's goal, visible hazards, missing information, and the outcome of previous actions. "
        "Evaluation follows three levels: {strong}response mode, risk understanding, and actionable handling{/strong}. "
        "A complete decision must pass every applicable check, linking the agent's judgement to a concrete course of action.",
        "识别危险场景只是机器人安全行为的一部分，智能体还需要判断用户的请求是否应当执行，以及如何执行。"
        "我们提出{strong}EmbodiSafety{/strong}，评测从理解视觉证据到制定后续行动的安全决策过程。"
        "任务要求模型结合用户目标、可见危险、缺失信息与此前动作的执行结果，给出恰当的响应。"
        "评测围绕{strong}响应模式、风险理解和可执行的安全处置{/strong}三个层级展开；"
        "只有全部适用检查均通过，才算完成一次安全决策，使模型的判断落实为具体的行动方案。",
    ),
]
