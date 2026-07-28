# jiaocheng 测试集

跑法：加载 jiaocheng skill，逐一执行场景，报告 PASS/FAIL。

---

## 测试 1：费曼中间态

concept difficulty=2，R1=fail, R2=pass, R3=fail。
走完所有轮次 → 判定：pass≥半数(2/3=yes) → mastered(deep)。

## 测试 2：费曼中间态不通过

concept difficulty=3，R1=fail, R2=fail, R3=pass, R4=fail, R5=fail。
走完 → pass<半数(1/5) → 普通卡壳 → 修复 → 重走未过轮次。

## 测试 3：换模式 mode_step 重置

费曼模式 R3，mode_step=3。用户说"换讲解"。→ mode_step=1，session_state 翻转。

## 测试 4：repair_count 天花板

concept repair_count=2，讲解模式费曼验证 fail → 诊断 → 修复 → repair_count=3 → 下次 fail → 强制放弃，不给拒绝选项。

## 测试 5：翻译无限循环防护

翻译模式 Step 5 fail × 3 → repair_count=3 → 强制放弃，标 abandoned。

## 测试 6：force_review 清除

spiral-track force_review=true，queue pending=0 → Session 结束复检第5项触发 → 设回 false。

## 测试 7：mastery_depth 缺失检测

concept mastery=mastered, mastery_depth=null → Session 结束复检第1项触发 → ❌ 阻断。

## 测试 8：四布尔互斥检测

session_state: in_feynman_drill=true, in_lecture=true → Session 结束复检第3项触发 → ❌ 阻断。

## 测试 9：shallow 守卫

concept mastery_depth="shallow", teaching_mode="feynman" → Session 启动第3项 → 强制从 R1 开始。

## 测试 10：already_know 验证幂等

self_assessed="already_know"，feynman_score=4（已通过快速验证），mastery=mastered → Session 启动第4项 → 跳过验证（不再重复验证）。
