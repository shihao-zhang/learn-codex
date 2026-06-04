## 1. OpenSpec 准备

- [x] 1.1 创建 `add-svg-diagram-gallery` OpenSpec change。
- [x] 1.2 定义范围、非目标、输入来源、图册规则、事实边界和验收要求。
- [x] 1.3 为 SVG 教学图册索引增加 spec delta。

## 2. 来源复核

- [x] 2.1 重新阅读 `AGENTS.md`。
- [x] 2.2 复核 `docs/diagram-style-guide.md`。
- [x] 2.3 盘点现有 `chapters/*/diagrams/*.svg` 和 companion Markdown 文件。
- [x] 2.4 复核 12 章 companion Markdown 的边界声明。

## 3. 图册索引

- [x] 3.1 新增 `docs/svg-diagram-gallery.md`。
- [x] 3.2 列出全部 12 章 SVG，包含章节、SVG 路径、companion Markdown 路径、理解问题和事实边界。
- [x] 3.3 保留 s08/s10 `待核实` 和 s12 `教学抽象` 边界。
- [x] 3.4 确认不改变章节状态。

## 4. 导航入口

- [x] 4.1 在 `README.md` 增加图册入口。
- [x] 4.2 确认不修改 `docs/fact-snapshot.md`、`docs/source-evidence.md` 或 `scripts/check_docs.py`。

## 5. 验收

- [x] 5.1 运行 `openspec validate add-svg-diagram-gallery --strict`。
- [x] 5.2 运行 `openspec validate --all --strict`。
- [x] 5.3 运行 `python3 scripts/check_docs.py`。
- [x] 5.4 运行 `python3 scripts/run_all.py`。
- [x] 5.5 运行 `python3 -m unittest discover -s tests`。
- [x] 5.6 运行 `git diff --check`。
- [x] 5.7 复核最终 diff，并在不 push 的前提下提交。
