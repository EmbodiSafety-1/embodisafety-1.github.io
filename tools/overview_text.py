"""Concise bilingual task introduction for the overview section."""

PARAGRAPHS = [
    (
        "Embodied agents must recognise environmental risks and choose a safe next step from visual evidence. "
        "We present EmbodiSafety, a benchmark with {strong}{tasks} decision tasks across {scenarios} visual scenarios{/strong}. "
        "Each task pairs a user instruction with one image or an ordered sequence of observations. "
        "{strong}Snapshot{/strong} comprises {snapshot} single-image tasks that require an immediate safety decision. "
        "{strong}Trajectory{/strong} comprises {trajectory} tasks with two to eight ordered frames, testing how agents respond to changing risks and execution failures. "
        "Agents select among six response modes—proceed, refuse, clarify, constrain, recover, and escalate—and explain the risk and the next safe action. "
        "Evaluation checks response selection, risk understanding, and actionable handling together.",
        "具身智能体需要根据视觉证据识别环境风险，并选择安全的下一步。"
        "我们提出 EmbodiSafety，包含{strong}{tasks}个决策任务，覆盖{scenarios}个视觉场景{/strong}。"
        "每个任务将用户指令与单张图像或有序观察序列配对。"
        "{strong}Snapshot{/strong} 包含{snapshot}个单图任务，要求模型根据当前场景作出即时安全决策；"
        "{strong}Trajectory{/strong} 包含{trajectory}个时序任务，提供2至8帧有序图像，考察模型如何应对变化的风险与执行失败。"
        "智能体需从执行、拒绝、澄清、约束执行、自主恢复和请求人工介入六种响应模式中作出选择，并说明风险与安全的后续行动。"
        "评测同时检查响应模式、风险理解与处置的可执行性。",
    ),
]
