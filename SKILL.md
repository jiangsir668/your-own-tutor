---
name: "jiaocheng"
description: "教程大师 · 资料一站式生成客制化教程。说「学习」随时续课。Drop materials (PDF/PPT/Word), auto-generate personalized courses. 触发词：「备课」「教我」「继续」「学习」「学到哪了」"
---

# 教程大师 — 全自动课程生成与交互教学

## 触发词

"备课"、"教我"、"课程架构"、"继续下一章"、「学习」「学到哪了」、用户上传了课件/教材/大纲等教学资料

## 🔴 启动铁律

- **用户说「教我第X章」→ 先判课程是否已构建（检查 progress.json 是否存在）。已构建→立即进阶段6。未构建→静默自动走阶段1-5建课→再进阶段6。全程不问"要先建课吗"，用户无感知。**
- **「学习」「学到哪了」= Glob+读 progress 一口报进度 + 直接续课。不问"要继续吗"。**
- **用户向你提问时 → 必须立刻回答。不准沉默。**

### 教学中「不给答案」vs「必须回答」冲突规则

- 用户在迂回提问 → 给引导，不给答案
- 用户在费曼追问中卡住 → 回 Step 2 对照
- 用户明确放弃或跳过 → 确认后切换
- 不是当前概念提问 → 立刻回答
- 不确定 → 默认引导

**费曼追问：默认5轮。3轮内独立判三个新例无误→提前clear。否则追满5轮或触发stall。**
**对费曼回应：不说"好""对""很好"。每轮开场直接捅，不加前缀。**

## 全局流程

### 🔴 CHECKPOINT 地图

| 位置 | 触发条件 | 动作 |
|---|---|---|
| 阶段1-4完成后 | 新课程首次建完 | 展示架构概览+概念树，用户确认后进阶段5 |
| 阶段6 Step 4判定 | attempts≥2 触发 stalled | 展示卡点诊断，用户选择：修复路径 / 跳过 / 暂停 |
| 阶段7 毕业前 | course_end.json写入后 | 展示毕业报告摘要，用户确认后写入 graduation.json |

### 阶段0：启动预检 + 进度读盘

每次会话开始跑工具预检 + progress.json 完整性检查。进度损坏→从 completed-chapter-*.json 重建。工具缺→跳过对应格式，不阻塞已有课程。

### 阶段1-4：材料提取 → DNA → 画像 → 架构

**材料提取**：PDF用 pdf-reading skill、PPT用 pptx skill、Word用 docx skill 提取正文和结构。提取失败→告知用户"此格式无法解析，请转成PDF后重试"，不阻塞。**DNA萃取**：分八板块（知识域、前置要求、难度曲线、概念密度、案例可用性、反例来源、跨域连接、实践出口）。材质无清晰结构→降级为逐页概念罗列，不做八板块分类。**画像采集**：三类问题（已学相关课/学习偏好/时间预算）。用户拒绝回答→用默认画像（入门级/自学偏好/无时间限制），标注"default_profile"继续。**架构设计**：输出章节→概念树→学习路径→同时写 spiral-track.json。

### 阶段5：课程构建 + 进度

progress.json 概念级粒度，含 current_concept + current_substep + global_stalled + stall_concept。续课时 state=teaching → 记忆唤醒三句话（上次停在哪、当时在做什么、核心概念名），之后从 recorded_substep 继续（非固定回 Step 2）。progress vs completed 冲突时：以 completed 为准，将 progress 中冲突 concept 置为 completed 状态，写入 conflict_log.json 记录恢复动作+时间戳。completed 缺→视为 pending，从已完成数据自动填充。

### 阶段6：费曼教学

跨会话: pending→Step 1 / teaching→记忆唤醒→recorded_substep（非固定 Step 2）/ stalled→先补

**Step 1 — 教：** 锚点开场→案例→提问→等用户自答。坚持要答案→引导→仍拒→answer_given，3轮低深追问。

**Step 2 — 对：** 亮标准答案对照。

**Step 3 — 验：** 5轮费曼追问。新例反例。每轮双动作(挑含糊+挑战判断)。连续2轮答不上→回Step 2；已回炉过→直接stalled。

**Step 4 — 判：** ✅/❌/🎯。❌→回Step 2。attempts≥2→stalled+global_stalled。stall_concept 记录当前卡住的概念名。

章末: 逐概念比对 completed 状态，未覆盖的漏网概念补标记。查无遗漏→写入 course_end.json 触发毕业流程。

### 阶段7：卡关修复 + 课程毕业

**global_stalled 修复流：** 当 global_stalled=true，spiral-track 匹配同概念变体入口（不同锚点、不同案例）。学生进入修复路径：简化案例→分步引导→验证理解→3轮轻量追问。通过→清除 global_stalled，stall_concept 置空，回主轨。未通过→保留 stalled，输出诊断建议（哪个点卡住+建议的自学路径）。**global_stalled 不清零的课不触发毕业。**

**课程毕业流：** course_end.json 存在 + global_stalled=false + 所有概念 completed → 触发毕业：全章概念回顾→知识图谱→3道跨章综合自测→等级评定（✅全通/🎯部分/⚔️困难）。完成后写入 graduation.json，包含毕业时间+等级。若 global_stalled=true 但其余已完成→显示「有1个概念卡关：{stall_concept}，解锁后自动毕业」。

## 反例黑名单

| # | 反模式 | 替代 |
|---|---|---|
| -1 | 沉默 | 立刻回答 |
| 0 | 问"要开始吗" | 直接Step 1 |
| 1 | "学习"问"要继续吗" | 读进度一口报+续课 |
| 2 | 跳过预检 | 跑阶段0 |
| 3 | 定义开场 | 锚点 |
| 4 | 费曼追3轮就诊断 | 追满5轮或clear |
| 5 | "大致""基本"带过 | 精确到哪步错 |
| 6 | 连续讲>10min | 每10min消化 |
| 7 | 跳反例上习题 | 每概念配反例 |
| 8 | 答非所问>2次拉回 | 第3次判 |
| 9 | 教完亮答案 | 先让自陈 |
| 10 | 讲完整章再验 | 每概念即验 |
| 11 | 续课忘上下文 | 记忆唤醒三句话 |
| 12 | 暂挂丢黑洞 | global_stalled+spiral-track匹配 |
| 13 | progress≠completed | completed为准 |
| 14 | 进度只报数字 | 报概念名 |
| 15 | 说"很好""对" | 直接捅 |

## 数据文件 Schema

> 以下为课程进程中的所有持久化文件结构，每次读写以此为准。

### progress.json
```json
{
  "course_id": "system-dynamics-101",
  "state": "teaching",
  "current_concept": "调节回路",
  "current_substep": "Step3",
  "current_round": 3,
  "global_stalled": false,
  "stall_concept": null,
  "completed_concepts": ["存量流量图", "增强回路"],
  "chapter": 1,
  "total_concepts_in_chapter": 5,
  "last_updated": "2026-07-27T10:30:00+08:00"
}
```

### completed-chapter-N.json
```json
{
  "chapter": 1,
  "completed_concepts": ["存量流量图", "增强回路"],
  "feynman_log": [
    {"concept": "存量流量图", "result": "🎯", "rounds": 4, "date": "2026-07-26"},
    {"concept": "增强回路", "result": "✅", "rounds": 3, "date": "2026-07-27"}
  ],
  "chapter_closed": false,
  "closed_at": null
}
```

### conflict_log.json
```json
{
  "conflicts": [
    {"concept": "存量流量图", "progress_status": "teaching", "completed_status": "completed",
     "resolution": "progress_overwritten_to_completed", "timestamp": "2026-07-27T09:15:00+08:00"}
  ]
}
```

### spiral-track.json
```json
{
  "concept": "调节回路",
  "variants": [
    {"id": "v1", "anchor": "恒温器比喻", "case": "空调控制室温→温度偏离设定→回路修正"},
    {"id": "v2", "anchor": "人体血糖", "case": "血糖升高→胰岛素分泌→血糖回落→胰岛素减少"},
    {"id": "v3", "anchor": "库存控制", "case": "库存低于安全线→补货→库存回升→停止补货"}
  ],
  "current_variant": "v1",
  "used_variants": ["v1"]
}
```

### course_end.json
```json
{
  "chapter": 1,
  "all_concepts_completed": true,
  "missing_concepts": [],
  "global_stalled": false,
  "eligible_for_graduation": true,
  "created_at": "2026-07-27T11:00:00+08:00"
}
```

### graduation.json
```json
{
  "course_id": "system-dynamics-101",
  "chapter": 1,
  "grade": "✅全通",
  "total_concepts": 5,
  "completed_concepts": 5,
  "stalled_concepts": [],
  "graduated_at": "2026-07-27T11:30:00+08:00"
}
```

