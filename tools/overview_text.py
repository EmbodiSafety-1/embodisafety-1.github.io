"""Copy for the overview intro paragraphs that sit under the native overview.

Both languages live here so they stay in sync, and every number is injected at
build time from the page's own sources: the task and track counts come from
assets/demos/manifest.json users in build_page.py, the scores from
tools/benchmark-results.json. Nothing in this file hard-codes a figure, so the
paragraphs can never drift from the leaderboard.

Markup markers: {strong}...{/strong} for emphasis, {em}...{/em} for the model name.
"""

PARAGRAPHS = [
    (
        "EmbodiSafety asks a practical question about embodied agents: before acting, do they notice the "
        "environmental risk in front of them, and does that understanding turn into a safe next step? "
        "The benchmark answers it with {strong}{tasks} decision tasks across {scenarios} visual "
        "scenarios{/strong}, drawn from homes, offices, hospitals, laboratories, and industrial floors. "
        "Each task pairs a user instruction with the visual evidence a robot would see and a reference "
        "decision, so a model is judged on what it observed, what it concluded, and what it chose to do next.",
        "EmbodiSafety 关注一个很实际的具身智能问题：在行动之前，机器人能否察觉眼前的环境风险，并把这种理解转化为安全的下一步？"
        "基准用{strong}{tasks}个决策任务、{scenarios}个视觉场景{/strong}来回答这个问题，覆盖家庭、办公室、医院、"
        "实验室和工业车间。每个任务都由一条用户指令、机器人实际看到的视觉证据和一份参考决策组成，"
        "模型的评测因此同时涉及它观察到了什么、判断出了什么，以及最终选择怎样行动。",
    ),
    (
        "The benchmark is split into two tracks. {strong}Snapshot{/strong} tasks, {snapshot} of the total, "
        "show a single image and ask for an immediate judgement: the scene is safe to act in, the request is "
        "harmful, the situation is underspecified and needs a clarifying question, or the goal can be met "
        "under explicit safety constraints. {strong}Trajectory{/strong} tasks, {trajectory} of the total, "
        "add two to eight ordered frames so the model sees how a situation develops while the task is carried "
        "out, including cases where an attempt fails and the robot has to recover on its own or stop and ask "
        "a person for help.",
        "基准分为两条任务线。{strong}Snapshot{/strong} 任务共 {snapshot} 个，只提供单张图像，要求模型给出即时判断："
        "场景可以安全执行、请求本身有害、信息不足需要追问，或是可以在明确的安全约束下完成目标。"
        "{strong}Trajectory{/strong} 任务共 {trajectory} 个，在此基础上提供2到8帧有序图像，"
        "让模型看到任务执行过程中局势如何变化，也包括多次尝试失败后需要自主恢复、或必须停下来请人接手的情形。",
    ),
    (
        "Every response is read on three levels. {strong}L1 checks the response mode{/strong}: does the model "
        "choose the action category the situation calls for? {strong}L2 checks the risk explanation{/strong}: "
        "is the hazard grounded in what is actually visible rather than in generic precautions? "
        "{strong}L3 checks the handling{/strong}: is the next step specific and actionable, including the "
        "clarifying question it promises or the constraints it promises to respect? A decision counts as "
        "complete only when every applicable check passes, so a fluent answer cannot pass on one strong "
        "field while the rest of the decision stays wrong.",
        "每条回答都从三个层级阅读。{strong}L1 检查响应模式{/strong}：模型是否选对了当前处境所要求的行动类别？"
        "{strong}L2 检查风险解释{/strong}：危险是否落在画面中真实可见的线索上，而不是泛泛的安全提醒？"
        "{strong}L3 检查处置{/strong}：下一步是否具体可执行，包括它承诺的澄清问题或将要遵守的约束？"
        "只有全部适用检查都通过的决策才算完整决策，这样可以避免某个字段写得漂亮、其余判断却错误的答案蒙混过关。",
    ),
    (
        "The scores separate recognising a hazard from responding to it. The strongest model on the page, "
        "{em}{best_model}{/em}, reaches {best_snapshot} complete-decision accuracy on Snapshot and "
        "{best_trajectory} on Trajectory, while the weakest embodied vision-language models sit at "
        "{low_snapshot} and {low_trajectory}. That gap is the point of the benchmark: a model can describe a "
        "scene fluently and still continue a request that should have been refused, constrained, or handed to "
        "a person. Snapshot and Trajectory are therefore reported side by side and never merged into one "
        "overall score.",
        "由此得到的分数把“识别风险”与“应对风险”区分开来。页面中最强的模型 {em}{best_model}{/em} "
        "在单图任务上的完整决策准确率为 {best_snapshot}，在时序任务上为 {best_trajectory}；"
        "而最弱的具身视觉语言模型只有 {low_snapshot} 和 {low_trajectory}。这正是基准要指出的差距："
        "模型可以把场景描述得很流畅，却仍然去执行一条本该被拒绝、被追加约束或转交人工的请求。"
        "也正因为如此，单图与时序成绩始终并列展示，而不会被合成一个总分。",
    ),
]
