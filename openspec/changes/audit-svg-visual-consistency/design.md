## Context

本仓 SVG 的长期规则已经由 `diagram-redraw-style-guide` 管理。现状不是缺少单张图规范，而是 12 张图跨批次完成后，需要确认它们作为一组材料时仍然可读、一致、边界保守。

关键约束：

- SVG 是教学辅助图，不是官方架构图。
- `FACT` 只能用于已经登记的固定 SHA / 官方资料 / release note / `docs/source-evidence.md` 可追溯机制。
- `待核实` 必须覆盖 s08/s10 和其他未闭环语义。
- s12 的综合图、pilot trace 和跨章节解释必须保持 `教学抽象`。
- 本次审计不触碰证据文件、章节状态和校验脚本。

## Audit Method

1. 收集全部目标文件：`chapters/*/diagrams/*.svg`。
2. 对全部 SVG 做 XML parse，先排除结构性错误。
3. 将全部 SVG 渲染为 PNG 或浏览器可视预览。
4. 逐张目视检查：
   - 文字和模块是否重叠。
   - 箭头、线条、chip 是否压住文字。
   - 第一阅读路径是否清楚。
   - 图例是否可读、不过重，并覆盖图中出现的语义。
   - `FACT` / `待核实` / `教学辅助` / `FAIL` / `DENY` / `RECOVERY` 标记是否和 style guide 一致。
5. 对 s08/s10/s12 做额外边界检查：
   - s08/s10 图中必须显式出现 `待核实`，且 companion Markdown 不能升级状态。
   - s12 图中必须显式出现 `教学抽象`，涉及 s08/s10 的边界继续保守。
6. 小问题直接修 SVG 和 companion Markdown；发现需要改变长期规则或事实状态的问题时暂停，不在本 change 内扩大范围。

## Repair Policy

可直接修：

- 轻微重排节点、箭头、chip、图例位置。
- 调整文案以消除遮挡或语义歧义，但不新增机制事实。
- 补充 companion Markdown 的 `Manual QA` 审计记录。
- 让已存在语义标记更一致，例如把图中已有教学表达显式标为 `教学辅助`。

不可直接修：

- 新增官方机制断言。
- 把 `待核实` 改成 `FACT`。
- 把 s12 的 `教学抽象` 改成官方架构表达。
- 修改 `docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py`。
- 改变章节 README 的状态或全仓事实边界。

## Output

本次审计的持久输出是：

- OpenSpec change 文档和 spec delta。
- 必要的小修后的 SVG / companion Markdown。
- `tasks.md` 中逐项记录 12 张 SVG 的视觉 QA 结论。
- 最终提交一个本地 commit，不 push。
